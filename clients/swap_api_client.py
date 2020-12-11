#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid
from .base_client import AnbbitClient
from .constants import OrderState, ANBBIT_API_HOST, SWAP_COMMON_PATH_PRIV, SWAP_COMMON_PATH_PUB
from .utils import get_cur_time_ms


class AnbbitSwapClient(AnbbitClient):

    def __init__(self, private_url_base=None, public_url_base=None, api_key=None, api_secret=None):
        private_url_base = private_url_base or ANBBIT_API_HOST + SWAP_COMMON_PATH_PRIV
        public_url_base = public_url_base or ANBBIT_API_HOST + SWAP_COMMON_PATH_PUB
        super(AnbbitSwapClient, self).__init__(private_url_base, public_url_base,
                                               api_key=api_key, api_secret=api_secret)

    def list_accounts(self):
        path = '/account/list'
        data = {}
        return self.private_post_request(path, data)

    def list_account_state(self, symbol):
        path = '/account/state'
        data = {
            'symbol': symbol
        }
        return self.private_post_request(path, data)

    def update_account_leverage(self, symbol, leverage, direction):
        path = '/account/leverage/update'
        data = {
            'symbol': symbol,
            'leverage': leverage,
            'direction': direction
        }
        return self.private_post_request(path, data)

    def list_position(self, symbol):
        path = '/position'
        data = {'symbol': symbol}
        return self.private_post_request(path, data)

    def create_order(self, symbol, qty, price, trade_type, amount=0, _type='limit', account_type='swap'):
        """
        cid: client define order id(uuid)
        """
        path = '/order/create'
        data = {
            'cid': 'cid_' + uuid.uuid1().hex,
            'symbol': symbol,
            'qty': qty,
            'price': price,
            'amount': amount,
            'type': _type,  # market_type
            'account_type': account_type,
            'trade_type': trade_type,
        }
        return self.private_post_request(path, data)

    def create_batch_order(self, symbol, orders: [], account_type='swap'):
        """
        orders = [{'cid': 'cid_' + uuid.uuid1().hex,
                'qty': qty,
                'price': price,
                'amount': amount,
                'type': _type,
                'trade_type': trade_type,
                },]
        """
        path = '/order/create/batch'
        data = {
            "symbol": symbol,
            "account_type": account_type,
            "orders": orders,
        }
        return self.private_post_request(path, data)

    def list_order_state(self, symbol, order_id):
        path = '/order/state'
        data = {
            'symbol': symbol,
            'order_id': order_id
        }
        return self.private_post_request(path, data)

    def cancel_order(self, order_id, symbol):
        path = '/order/cancel'
        data = {
            'order_id': order_id,
            'symbol': symbol,
        }
        return self.private_post_request(path, data)

    def cancel_all_order(self, symbol):
        path = '/order/cancel/all'
        data = {
            'symbol': symbol,
        }
        return self.private_post_request(path, data)

    def cancel_batch_order(self, symbol, order_ids: []):
        path = '/order/cancel/batch'
        data = {
            'symbol': symbol,
            'order_ids': order_ids,
        }
        return self.private_post_request(path, data)

    def list_active_order(self, symbol, account_type=None, state=None, trade_type=None, page=1, size=10):
        path = '/order/active/list'
        data = {
            "symbol": symbol,
            "account_type": account_type,
            # "type": market_type,
            "state": state,
            "trade_type": trade_type,
            "page": page,
            "size": size,
            'end_tm_ms': get_cur_time_ms(),
        }
        if data.get('state'):
            assert data['state'] in OrderState.ORDER_STATE_OPEN

        return self.private_post_request(path, data)

    def list_history_order(self, symbol, account_type=None, order_type=None, order_state=None, trade_type=None, page=1,
                           size=10):
        path = '/order/history/list'
        data = {
            "symbol": symbol,
            "account_type": account_type,
            "order_type": order_type,
            "order_state": order_state,
            "trade_type": trade_type,
            "page": page,
            "size": size,
            'end_tm_ms': get_cur_time_ms(),
        }
        if data.get('order_state'):
            assert data['order_state'] in OrderState.ORDER_STATE_CLOSED

        return self.private_post_request(path, data)

    def list_trade_list(self, symbol):
        path = '/trade/list'
        data = {
            'symbol': symbol,
            'start_tm_ms': 0,
            'end_tm_ms': get_cur_time_ms(),
        }
        return self.private_post_request(path, data)

    def list_balance(self, symbol):
        path = '/balance'
        data = {
            'symbol': symbol,
        }
        return self.private_post_request(path, data)

    def list_balance_list(self):
        path = '/balance/list'
        return self.private_post_request(path)

    def list_symbol(self):
        path = '/symbol/list'
        return self.public_request(path)

    def get_index_price(self, symbol):
        path = f'/index/{symbol}'
        return self.public_request(path)
