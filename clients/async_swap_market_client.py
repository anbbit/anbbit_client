#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base_client import AsyncAnbbitClient
from .constants import ANBBIT_MARKET_HOST, SWAP_COMMON_PATH_PUB


class AnbbitSwapMarketClient(AsyncAnbbitClient):

    def __init__(self, public_url_base=None):
        public_url_base = public_url_base or ANBBIT_MARKET_HOST + SWAP_COMMON_PATH_PUB
        super(AnbbitSwapMarketClient, self).__init__(None, public_url_base, api_key=None, api_secret=None)

    async def market_orderbook(self, symbol, level='ALL'):
        path = f'/market/orderbook/{symbol}/{level}'
        return await self.public_request(path)

    async def market_trade(self, symbol):
        path = f'/market/trade/{symbol}'
        return await self.public_request(path)

    async def market_ticker(self, symbol):
        path = f'/market/ticker/{symbol}'
        return await self.public_request(path)

    async def market_kline(self, symbol, interval, begin_tm=None, end_tm=None):
        path = f'/market/kline/{symbol}/{interval}'
        params = {}
        if begin_tm:
            params['begin'] = begin_tm
        if end_tm:
            params['end'] = end_tm
        return await self.public_request(path, params=params)
