#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import logging
import asyncio
import aiohttp
from aiohttp import WSMsgType

from .utils import get_cur_time_secs
from .constants import WsConf


class AnbbitWsClient(object):
    def __init__(self, url, timeout_sec=30, ping_msg=WsConf.PING_MSG, **kwargs):
        self.url = url
        self.timeout_sec = timeout_sec
        self.ws = None
        self.last_recv_tm_sec = 0  # use to determine is ws is still alive or not
        self.max_no_msg_interval_sec = WsConf.MAX_NO_MSG_INTERVAL_SEC  # consider ws is dead
        self.ping_msg = ping_msg
        self.heartbeat_sec = WsConf.PING_INTERVAL_SEC
        self.is_connecting = False
        self.retry_times = 0
        self.is_debug = kwargs.get('is_debug')

        self.initialize(**kwargs)

        asyncio.ensure_future(self.reconnect())
        asyncio.ensure_future(self.check_alive())
        if self.ping_msg:
            # User Define Ping msg(Usually text type)
            asyncio.ensure_future(self.keep_alive())

    def initialize(self, **kwargs):
        """Hook for subclass initialization. Called for on object init
        """
        pass

    async def connect(self):
        print(f"ws_url={self.url} connecting...")
        try:
            session = aiohttp.ClientSession(conn_timeout=self.timeout_sec, read_timeout=self.timeout_sec,
                                            trust_env=self.is_debug)
            self.ws = await session.ws_connect(self.url, heartbeat=self.heartbeat_sec)
            await self.on_connected()
            asyncio.ensure_future(self.run())
        except Exception as e:
            logging.error(f"connection error={str(e)}")

    async def run(self):
        while True:
            msg = await self.ws.receive()
            if msg.type in (WSMsgType.CLOSE, WSMsgType.ERROR):
                logging.error(f"connection closed, msg={msg}")
                break

            if msg.data is None:
                logging.error(f"msg.data is None, msg={msg}")
                break

            self.last_recv_tm_sec = get_cur_time_secs()
            try:
                await self.on_message(msg.data)
            except Exception as ex:
                logging.error(f"on_message exception={ex}, msg={msg}")

        if self.ws:
            await self.ws.close()
        self.ws = None
        await self.on_closed()

        asyncio.ensure_future(self.reconnect())

    async def on_connected(self):
        print('on_connected')

    async def on_message(self, msg):
        print(f'on_message msg={msg}')

    async def on_closed(self):
        print(f'on_closed')
        pass

    def is_dead(self):
        return not self.ws or (get_cur_time_secs() - self.last_recv_tm_sec) > self.max_no_msg_interval_sec

    async def reconnect(self):
        if self.is_connecting:
            return

        self.is_connecting = True
        self.ws = None
        MAX_TIMES = 2
        while not self.ws:
            retry_times = min(self.retry_times, MAX_TIMES)
            delay_tm_sec = 2**retry_times - 1
            logging.error(f"reconnecting... after={delay_tm_sec} sec, retry_times={self.retry_times}")

            self.retry_times += 1
            await asyncio.sleep(delay_tm_sec)
            await self.connect()

        self.retry_times = 0
        self.is_connecting = False

    async def keep_alive(self):
        while True:
            await asyncio.sleep(self.heartbeat_sec)

            try:
                # send text ping msg
                await self.ws.send_str(self.ping_msg)
            except Exception as ex:
                await self.reconnect()

    async def check_alive(self):
        """A ws watchdog"""
        while True:
            await asyncio.sleep(WsConf.CHECK_INTERVAL_SEC)
            try:
                if self.is_dead():
                    logging.error("check_alive ws is dead")
                    await self.reconnect()
            except Exception as ex:
                pass

    async def send(self, msg):
        if isinstance(msg, dict):
            msg_str = json.dumps(msg)
        elif isinstance(msg, str):
            msg_str = msg
        else:
            raise TypeError()

        await self.ws.send_str(msg_str)
