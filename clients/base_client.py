#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hmac
import json
import requests
import aiohttp
from hashlib import sha256
from .utils import get_cur_time_ms
from .constants import Status


class AnbbitClient(object):

    def __init__(self, private_url_base, public_url_base, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.private_url_base = private_url_base
        self.public_url_base = public_url_base

    @staticmethod
    def signature(api_secret, data):
        return hmac.new(api_secret, data, sha256).hexdigest()

    @staticmethod
    def get_data_str(data=None):
        """Add nonce to data dict and format to compact str type"""
        data = data or {}
        data['nonce'] = get_cur_time_ms()
        return json.dumps(data, separators=(',', ':'))

    def get_signed_headers(self, data):
        return {
            'api-key': self.api_key,
            'signature': self.signature(self.api_secret.encode('utf8'), data.encode('utf8')),
        }

    @staticmethod
    def send_request(url, json=None, params=None, data=None, method='POST', headers=None):
        ret = requests.request(method=method, url=url, params=params, json=json, data=data, headers=headers)
        print(f'send_request, url={ret.url}')
        if ret.status_code == 200:
            return ret.json()
        else:
            err_msg = 'Something unexpected happened! http status_code=%s' % ret.status_code
            print(err_msg)
            raise Exception(err_msg)

    def private_post_request(self, path, data=None):
        url = self.private_url_base + path
        data_str = self.get_data_str(data)
        signed_headers = self.get_signed_headers(data_str)
        ret = self.send_request(url, data=data_str, headers=signed_headers)
        if ret['status'] == Status.STATUS_SUCCESS:
            try:
                return ret['data']
            except KeyError:
                # if result No need to response data
                return None
        else:
            raise Exception(ret)

    def signature_test(self):
        path = '/test'
        return self.private_post_request(path)

    def public_request(self, path, params=None, data=None, method='GET'):
        url = self.public_url_base + path
        data_str = json.dumps(data, separators=(',', ':')) if data else None
        ret = self.send_request(url, params=params, data=data_str, method=method)
        if ret['status'] == Status.STATUS_SUCCESS:
            try:
                return ret['data']
            except KeyError:
                # if result No need to response data
                return None
        else:
            raise Exception(ret)


class AsyncAnbbitClient(AnbbitClient):

    @staticmethod
    async def send_request(url, json=None, params=None, data=None, method='POST', headers=None):
        async with aiohttp.ClientSession() as session:
            async with session.request(method=method, url=url, json=json, params=params,
                                       data=data, headers=headers) as response:
                print(f'send_request, url={response.url}')
                ret = await response.json()
            return ret

    async def private_post_request(self, path, data=None):
        url = self.private_url_base + path
        data_str = self.get_data_str(data)
        signed_headers = self.get_signed_headers(data_str)
        result = await self.send_request(url, data=data_str, headers=signed_headers)
        if result['status'] == Status.STATUS_SUCCESS:
            try:
                return result['data']
            except KeyError:
                # if not data to response
                return None
        else:
            raise Exception(result)

    async def public_request(self, path, params=None, data=None, method='GET'):
        url = self.public_url_base + path
        data_str = json.dumps(data, separators=(',', ':')) if data else None
        result = await self.send_request(url, params=params, data=data_str, method=method)
        if result['status'] == Status.STATUS_SUCCESS:
            try:
                return result['data']
            except KeyError:
                # if result No need to response data
                return None
        else:
            raise Exception(result)
