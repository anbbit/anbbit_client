#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid
from .base_client import AsyncAnbbitClient
from .constants import OrderState, ANBBIT_API_HOST, SPOT_API_PATH_PRIV, SPOT_API_PATH_PUB, TM_MS_ONE_DAY
from .utils import get_cur_time_ms


class AnbbitSpotClient(AsyncAnbbitClient):
    """
    Use api_key/api_secret as auth
    """

    def __init__(self, private_url_base=None, public_url_base=None, api_key=None, api_secret=None):
        private_url_base = private_url_base or ANBBIT_API_HOST + SPOT_API_PATH_PRIV
        public_url_base = public_url_base or ANBBIT_API_HOST + SPOT_API_PATH_PUB
        super(AnbbitSpotClient, self).__init__(private_url_base, public_url_base, api_key, api_secret)

    async def get_balance(self, account_type='trading'):
        path = '/balance'
        data = {
            'currency': "BTC",
            'account_type': account_type,  # default account_type=trading
        }
        return await self.private_post_request(path, data=data)

    async def list_balance(self, account_type='trading'):
        path = '/balance/list'
        data = {
            'account_type': account_type,  # default account_type=trading
        }
        return await self.private_post_request(path, data=data)

    async def create_order(self, symbol, side, qty, price, _type='limit'):
        path = '/order/create'
        # cid: client define order id(uuid)
        data = {
            'cid': 'cid_' + uuid.uuid4().hex,
            'symbol': symbol,
            'side': side,
            'qty': qty,
            'price': price,
            'type': _type,
        }
        return await self.private_post_request(path, data=data)

    async def get_order_state(self, order_id, symbol):
        path = '/order/state'
        data = {
            'order_id': order_id,
            'symbol': symbol,
        }
        return await self.private_post_request(path, data=data)

    async def cancel_order(self, order_id, symbol):
        path = '/order/cancel'
        data = {
            'order_id': order_id,
            'symbol': symbol,
        }
        return await self.private_post_request(path, data=data)

    async def list_active_order(self, symbol):
        path = '/order/active/list'
        data = {
            'state': '',
            'side': '',
            'symbol': symbol,
            'start_tm_ms': 0,
            'end_tm_ms': get_cur_time_ms(),
            'limit': 20
        }
        if data['state']:
            assert data['state'] in OrderState.ORDER_STATE_OPEN

        return await self.private_post_request(path, data=data)

    async def list_history_order(self, symbol):
        path = '/order/history/list'
        end_tm_ms = get_cur_time_ms()
        start_tm_ms = end_tm_ms - TM_MS_ONE_DAY
        data = {
            'state': '',
            'side': '',
            'symbol': symbol,
            'start_tm_ms': start_tm_ms,
            'end_tm_ms': end_tm_ms,
            'limit': 20
        }
        if data['state']:
            assert data['state'] in OrderState.ORDER_STATE_CLOSED

        return await self.private_post_request(path, data=data)

    async def list_trade(self, symbol):
        path = '/trade/list'
        end_tm_ms = get_cur_time_ms()
        start_tm_ms = end_tm_ms - TM_MS_ONE_DAY
        data = {
            'symbol': symbol,
            'start_tm_ms': start_tm_ms,
            'end_tm_ms': end_tm_ms,
            'limit': 20
        }
        return await self.private_post_request(path, data=data)

    async def get_timestamp_ms(self):
        path = '/timestamp'
        return await self.public_request(path)

    async def list_symbol(self):
        path = '/symbol/list'
        return await self.public_request(path)

    async def list_currency(self):
        path = '/currency/list'
        return await self.public_request(path)

    async def get_index_price(self, symbol):
        path = f'/index/{symbol}'
        return await self.public_request(path)
