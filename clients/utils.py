#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
from time import time


def get_cur_time_ms():
    """
    return current timestamp in milliseconds
    """
    return int(time() * 1000)


def get_cur_time_secs():
    '''
    return current timestamp_handler in seconds
    '''
    return int(time())


def run_sync(future, loop=None):
    loop = loop or asyncio.get_event_loop()
    return loop.run_until_complete(future)
