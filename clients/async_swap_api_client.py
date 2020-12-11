#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid
from .base_client import AsyncAnbbitClient
from .constants import OrderState, ANBBIT_API_HOST, SWAP_COMMON_PATH_PRIV, SWAP_COMMON_PATH_PUB
from .utils import get_cur_time_ms


class SwapAnbbitClient(AsyncAnbbitClient):

    def __init__(self, private_url_base=None, public_url_base=None, api_key=None, api_secret=None):
        private_url_base = private_url_base or ANBBIT_API_HOST + SWAP_COMMON_PATH_PRIV
        public_url_base = public_url_base or ANBBIT_API_HOST + SWAP_COMMON_PATH_PUB
        super(SwapAnbbitClient, self).__init__(private_url_base, public_url_base,
                                               api_key=api_key, api_secret=api_secret)

    async def list_account_list(self, symbol):
        path = '/account/list'
        data = {
            'symbol': symbol
        }
        return await self.private_post_request(path, data)

    # 合约账户详情
    async def list_account_state(self):
        path = '/account/state'
        data = {}
        return await self.private_post_request(path, data)

    async def update_account_leverage(self, symbol, leverage, direction):
        path = '/account/leverage/update'
        data = {
            'symbol': symbol,
            'leverage': leverage,
            'direction': direction
        }
        return await self.private_post_request(path, data)

    async def list_position(self, symbol):
        path = '/position'
        data = {'symbol': symbol}
        return await self.private_post_request(path, data)

    async def create_order(self, symbol, qty, price, trade_type, amount=0, _type='limit', account_type='swap'):
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
        return await self.private_post_request(path, data)

    async def create_batch_order(self, symbol, orders: [], account_type='swap'):
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
        return await self.private_post_request(path, data)

    async def list_order_state(self, symbol, order_id):
        path = '/order/state'
        data = {
            'symbol': symbol,
            'order_id': order_id
        }
        return await self.private_post_request(path, data)

    async def cancel_order(self, order_id, symbol):
        path = '/order/cancel'
        data = {
            'order_id': order_id,
            'symbol': symbol,
        }
        return await self.private_post_request(path, data)

    async def cancel_all_order(self, symbol):
        path = '/order/cancel/all'
        data = {
            'symbol': symbol,
        }
        return await self.private_post_request(path, data)

    async def cancel_batch_order(self, symbol, order_ids: []):
        path = '/order/cancel/batch'
        data = {
            'symbol': symbol,
            'order_ids': order_ids,
        }
        return await self.private_post_request(path, data)

    async def list_active_order(self, symbol, account_type=None, state=None, trade_type=None, page=1, size=10):
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

        return await self.private_post_request(path, data)

    async def list_history_order(self, symbol):
        path = '/order/active/list'
        data = {
            'state': '',
            'side': '',
            'symbol': symbol,
            'start_tm_ms': 0,
            'end_tm_ms': get_cur_time_ms(),
            'limit': 100
        }
        if data.get('state'):
            assert data['state'] in OrderState.ORDER_STATE_CLOSED

        return await self.private_post_request(path, data)

    async def list_trade_list(self, symbol):
        path = '/trade/list'
        data = {
            'symbol': symbol,
            'start_tm_ms': 0,
            'end_tm_ms': get_cur_time_ms(),
        }
        return await self.private_post_request(path, data)

    async def list_balance(self, symbol):
        path = '/balance'
        data = {
            'symbol': symbol,
        }
        return await self.private_post_request(path, data)

    async def list_balance_list(self):
        path = '/balance/list'
        return await self.private_post_request(path)

    async def list_symbol(self):
        path = '/symbol/list'
        return await self.public_request(path)

    async def get_index_price(self, symbol):
        path = f'/index/{symbol}'
        return await self.public_request(path)
