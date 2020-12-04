#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base_client import AnbbitClient
from .constants import ANBBIT_MARKET_HOST, SWAP_COMMON_PATH_PUB


class AnbbitSwapMarketClient(AnbbitClient):

    def __init__(self, public_url_base=None):
        public_url_base = public_url_base or ANBBIT_MARKET_HOST + SWAP_COMMON_PATH_PUB
        super(AnbbitSwapMarketClient, self).__init__(None, public_url_base, api_key=None, api_secret=None)

    def market_orderbook(self, symbol, level='ALL'):
        path = f'/market/orderbook/{symbol}/{level}'
        print(f'market_orderbook path={path}')
        return self.public_request(path)

    def market_trade(self, symbol):
        path = f'/market/trade/{symbol}'
        print(f'market_trade path={path}')
        return self.public_request(path)

    def market_ticker(self, symbol):
        path = f'/market/ticker/{symbol}'
        print(f'market_ticker path={path}')
        return self.public_request(path)

    def market_kline(self, symbol, interval, begin_tm=None, end_tm=None):
        path = f'/market/kline/{symbol}/{interval}'
        params = {}
        if begin_tm:
            params['begin'] = begin_tm
        if end_tm:
            params['end'] = end_tm
        print(f'market_kline path={path}, params={params}')
        return self.public_request(path, params=params)
