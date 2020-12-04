#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid
from .base_client import AsyncAnbbitClient
from .constants import OrderState, ANBBIT_API_HOST, SPOT_API_PATH_PRIV, SPOT_API_PATH_PUB
from .utils import get_cur_time_ms


class AnbbitSpotClient(AsyncAnbbitClient):
    """
    Use api_key/api_secret as auth
    """

    def __init__(self, private_url_base=None, public_url_base=None, api_key=None, api_secret=None):
        private_url_base = private_url_base or ANBBIT_API_HOST + SPOT_API_PATH_PRIV
        public_url_base = public_url_base or ANBBIT_API_HOST + SPOT_API_PATH_PUB
        super(AnbbitSpotClient, self).__init__(private_url_base, public_url_base, api_key, api_secret)

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
