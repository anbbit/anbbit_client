#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid
from .base_client import AnbbitClient
from .constants import OrderState, ANBBIT_API_HOST, SPOT_API_PATH_PRIV, SPOT_API_PATH_PUB, TM_MS_ONE_DAY
from .utils import get_cur_time_ms


class AnbbitSpotClient(AnbbitClient):
    """
    Use api_key/api_secret as auth
    """

    def __init__(self, private_url_base=None, public_url_base=None, api_key=None, api_secret=None):
        private_url_base = private_url_base or ANBBIT_API_HOST + SPOT_API_PATH_PRIV
        public_url_base = public_url_base or ANBBIT_API_HOST + SPOT_API_PATH_PUB
        super(AnbbitSpotClient, self).__init__(private_url_base, public_url_base, api_key, api_secret)

    def get_balance(self, account_type='trading', currency='BTC'):
        path = '/balance'
        data = {
            'currency': currency,
            'account_type': account_type,  # default account_type=trading
        }
        return self.private_post_request(path, data=data)

    def list_balance(self, account_type='trading'):
        path = '/balance/list'
        data = {
            'account_type': account_type,  # default account_type=trading
        }
        return self.private_post_request(path, data=data)

    def create_order(self, symbol, side, qty, price, _type='limit'):
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
        return self.private_post_request(path, data=data)

    def get_order_state(self, order_id, symbol):
        path = '/order/state'
        data = {
            'order_id': order_id,
            'symbol': symbol,
        }
        return self.private_post_request(path, data=data)

    def cancel_order(self, order_id, symbol):
        path = '/order/cancel'
        data = {
            'order_id': order_id,
            'symbol': symbol,
        }
        return self.private_post_request(path, data=data)

    def list_active_order(self, symbol):
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

        return self.private_post_request(path, data=data)

    def list_history_order(self, symbol):
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

        return self.private_post_request(path, data=data)

    def list_trade(self, symbol):
        path = '/trade/list'
        end_tm_ms = get_cur_time_ms()
        start_tm_ms = end_tm_ms - TM_MS_ONE_DAY
        data = {
            'symbol': symbol,
            'start_tm_ms': start_tm_ms,
            'end_tm_ms': end_tm_ms,
            'limit': 20
        }
        return self.private_post_request(path, data=data)

    def get_timestamp_ms(self):
        path = '/timestamp'
        return self.public_request(path)

    def list_symbol(self):
        path = '/symbol/list'
        return self.public_request(path)

    def list_currency(self):
        path = '/currency/list'
        return self.public_request(path)

    def get_index_price(self, symbol):
        path = f'/index/{symbol}'
        return self.public_request(path)
