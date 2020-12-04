#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid
from .base_client import AnbbitClient
from .constants import OrderState, ANBBIT_API_HOST, SPOT_API_PATH_PRIV, SPOT_API_PATH_PUB
from .utils import get_cur_time_ms


class AnbbitSpotClient(AnbbitClient):
    """
    Use api_key/api_secret as auth
    """

    def __init__(self, private_url_base=None, public_url_base=None, api_key=None, api_secret=None):
        private_url_base = private_url_base or ANBBIT_API_HOST + SPOT_API_PATH_PRIV
        public_url_base = public_url_base or ANBBIT_API_HOST + SPOT_API_PATH_PUB
        super(AnbbitSpotClient, self).__init__(private_url_base, public_url_base, api_key, api_secret)

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
