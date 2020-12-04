#!/usr/bin/env python
# -*- coding: utf-8 -*-

from builtins import zip
from decimal import Decimal

MAX_TRADE_FEE_RATE = Decimal("0.005")
MIN_TRADE_FEE_RATE = Decimal("-0.005")
FAK_RATE = 0.03

ANBBIT_API_HOST = 'https://api.anbbit.com'
ANBBIT_MARKET_HOST = 'https://market.anbbit.com'

ANBBIT_SPOT_WS_HOST = 'wss://ws.anbbit.com/bitan/stream'
ANBBIT_SWAP_WS_HOST = 'wss://ws.anbbit.com/swap/v2/sub'

SPOT_API_PATH_PRIV = '/api/v1/private'
SPOT_API_PATH_PUB = '/api/v1/public'

SPOT_MARKET_PATH_PUB = '/bitan/api/v3'

SWAP_COMMON_PATH_PRIV = '/api/swap/v1/private'
SWAP_COMMON_PATH_PUB = '/api/swap/v1/public'


class Status:
    STATUS_UNKNOWN = -1
    STATUS_SUCCESS = 0
    STATUS_ERROR = 1
    STATUS_USER_OR_PWD_INVALID = 2
    STATUS_NOT_LOGIN = 3
    STATUS_ILLEGAL_PARAMETER = 4
    STATUS_GEETEST_VALIDATE_FAILED = 5
    STATUS_INVALID_QUERY = 6
    STATUS_UPSERT_DB_FAILED = 7
    STATUS_INSERT_DB_FAILED = 8

    # account 1000-1099
    STATUS_PASSWORD_TOO_SHORT = 1000
    STATUS_INVALID_EMAIL = 1001
    STATUS_INVALID_PHONE = 1002
    STATUS_INVALID_REGISTER_CODE = 1003
    STATUS_ACCOUNT_ALREADY_EXIST = 1004
    STATUS_ACCOUNT_NOT_EXIST = 1005
    STATUS_ACCOUNT_OR_PASSWORD_WRONG = 1006
    STATUS_ACCOUNT_STATE_NOT_REGISTERING = 1007
    STATUS_ACCOUNT_REGISTER_CODE_SEND_TO_QUICK = 1008
    STATUS_INVALID_INVITE_CODE = 1009
    STATUS_ACCOUNT_STATE_NOT_NORMAL = 1010
    STATUS_UPDATE_PASSWD_FAILED = 1011
    STATUS_ACCOUNT_SIGN_UP_FAILED = 1012

    # symbol 1100-1199
    STATUS_SYMBOL_NOT_EXIST = 1100
    STATUS_INSERT_SYMBOL_FAVOR_FAILED = 1101
    STATUS_DELETE_SYMBOL_FAVOR_FAILED = 1102

    # order 1200-1299
    STATUS_ORDER_STATE_NOT_EXIST = 1200

    # wallet 1300-1399
    STATUS_DEPOSIT_ADDRESS_NOT_EXIST = 1300
    STATUS_DEPOSIT_NOT_PENDING = 1301
    STATUS_DEPOSIT_AMOUNT_ILLEGAL = 1302
    STATUS_USER_WALLET_NOT_EXIST = 1303
    STATUS_DEPOSIT_NO_BALANCE_NEED_TO_UPDATE = 1304
    STATUS_CHAIN_EOS_WITHOUT_MEMO = 1305
    STATUS_DEPOSIT_NO_BALANCE_UPDATED = 1306
    STATUS_USER_WALLET_CREATE_FAILED = 1307
    STATUS_USER_WALLET_ILLEGAL = 1308
    STATUS_CURRENCY_CONFIG_NOT_EXIST = 1309
    STATUS_CURRENCY_NOT_DEPOSITABLE = 1310
    STATUS_WITHDRAW_ADDRESS_INSERT_FAILED = 1311
    STATUS_WITHDRAW_ADDRESS_NOT_EXIST = 1312
    STATUS_WITHDRAW_ADDRESS_APPLY_FAILED = 1313
    STATUS_DEPOSIT_ADDRESS_INSERT_FAILED = 1314
    STATUS_CURRENCY_ADDRESS_CONFIG_NOT_EXIST = 1315

    # API KEY
    STATUS_APIKEY_NOT_EXIST = 2000
    STATUS_APIKEY_REQUIRE_SIGN = 2001
    STATUS_APIKEY_SIGN_FAILED = 2002
    STATUS_APIKEY_NO_KEY = 2003
    STATUS_APIKEY_NO_SIGN = 2004
    STATUS_APIKEY_NO_NONCE = 2005
    STATUS_APIKEY_NONCE_INVALID = 2006
    STATUS_APIKEY_EXCEED_REQ_LIMIT = 2007
    STATUS_APIKEY_NO_TIMESTAMP = 2008

    STATUS_WALLET_INVALID_ADDRESS = 10001
    STATUS_WALLET_KEYSTORE_FILE_ERROR = 10002
    STATUS_WALLET_KEYSTORE_FILE_NOT_EXIST = 10003
    STATUS_WALLET_SIGN_ERROR = 10004
    STATUS_WALLET_REQUEST_FAILED = 10005
    STATUS_WALLET_RESPONSE_FAILED = 10006
    STATUS_WALLET_FUND_ADDRESS_INSUFFICIENT = 10007
    STATUS_WALLET_UNSUPPORTED_CURRENCY = 10008
    STATUS_WALLET_TRANSACTION_EXIST = 10009
    STATUS_WALLET_ADDRESS_NOT_FOUND = 10010
    STATUS_WALLET_ADDRESS_NONCE_FAILED = 10011
    STATUS_WALLET_FUND_ADDRESS_NOT_FOUND = 10012
    STATUS_WALLET_OTHER_ERROR = 10013
    STATUS_WALLET_BALANCE_INSUFFICIENT = 10014
    STATUS_WALLET_NONCE_INSERT_FAILED = 10015
    STATUS_WALLET_MINE_ADDRESS_INSUFFICIENT = 10016
    STATUS_WALLET_UNSUPPORTED_CHAIN_NAME = 10017
    STATUS_WALLET_SAVE_SIGNATURE_ERROR = 10018

    STATUS_WALLET_CONTRACT_DECIMALS_ERROR = 10020
    STATUS_WALLET_CREATE_CURRENCY_CONFIG_ERROR = 10021

    STATUS_MSG_MAP = {
        STATUS_UNKNOWN: "Unknown error",
        STATUS_SUCCESS: "ok",
        STATUS_ERROR: "error",
        STATUS_USER_OR_PWD_INVALID: "invalid",
        STATUS_NOT_LOGIN: "user_not_login",
        STATUS_ILLEGAL_PARAMETER: "illegal parameter",
        STATUS_GEETEST_VALIDATE_FAILED: "geetest validate failed",
        STATUS_INVALID_QUERY: "invalid query",

        STATUS_APIKEY_NOT_EXIST: "api key is not exist",
        STATUS_APIKEY_REQUIRE_SIGN: "api key require sign",
        STATUS_APIKEY_SIGN_FAILED: "sign failed",
        STATUS_APIKEY_NO_KEY: "not found api key",
        STATUS_APIKEY_NO_SIGN: "not found sign content",
        STATUS_APIKEY_NO_NONCE: "not found nonce",
        STATUS_APIKEY_NONCE_INVALID: "nonce is invalid",
        STATUS_APIKEY_EXCEED_REQ_LIMIT: "request exceed limit",
        STATUS_APIKEY_NO_TIMESTAMP: "not found timestamp",

        STATUS_WALLET_INVALID_ADDRESS: "wallet address is invalid",
        STATUS_WALLET_KEYSTORE_FILE_ERROR: "not found wallet file",
        STATUS_WALLET_KEYSTORE_FILE_NOT_EXIST: "wallet file is not exist",
        STATUS_WALLET_SIGN_ERROR: "sign error",
        STATUS_WALLET_REQUEST_FAILED: "request failed",
        STATUS_WALLET_RESPONSE_FAILED: "response failed",
        STATUS_WALLET_FUND_ADDRESS_INSUFFICIENT: "fund address balance insufficient",
        STATUS_WALLET_UNSUPPORTED_CURRENCY: "coin is not support",
        STATUS_WALLET_TRANSACTION_EXIST: "transaction is exist",
        STATUS_WALLET_ADDRESS_NOT_FOUND: "wallet get address failed",
        STATUS_WALLET_ADDRESS_NONCE_FAILED: "address nonce get failed",
        STATUS_WALLET_FUND_ADDRESS_NOT_FOUND: "fund address not found",
        STATUS_WALLET_OTHER_ERROR: "other error",
        STATUS_WALLET_BALANCE_INSUFFICIENT: "wallet balance not enough",
        STATUS_WALLET_NONCE_INSERT_FAILED: "address nonce insert failed",
        STATUS_WALLET_MINE_ADDRESS_INSUFFICIENT: "mine address balance insufficient",
        STATUS_WALLET_UNSUPPORTED_CHAIN_NAME: "unsupported chain",
        STATUS_WALLET_SAVE_SIGNATURE_ERROR: "save signature into DB error",

        STATUS_WALLET_CONTRACT_DECIMALS_ERROR: "Contract decimals error",
        STATUS_WALLET_CREATE_CURRENCY_CONFIG_ERROR: "Create currency config errro"
    }


class WsConf:
    CHAN_ORDERBOOK = "orderbook.{symbol}.{level}"
    CHAN_TRADE = "trade.{symbol}"
    CHAN_TICKER = "ticker.{symbol}"
    CHAN_KLINE = "kline.{symbol}.{kline_interval}"

    KLINE_INTERVAL_1M = "1m"
    KLINE_INTERVAL_3M = "3m"

    PING_INTERVAL_SEC = 30
    MAX_NO_MSG_INTERVAL_SEC = 30
    CHECK_INTERVAL_SEC = 10

    PING_MSG = "PING"
    PONG_RES = "PONG"
    WELLCOME = "hello"


class OrderState:
    ORDER_STATE_PENDING_SUBMIT_STR = "pending_submit"
    ORDER_STATE_SUBMITTED_STR = "submitted"
    ORDER_STATE_PARTIAL_FILLED_STR = "partial_filled"
    ORDER_STATE_PARTIAL_CANCELED_STR = "partial_canceled"
    ORDER_STATE_FILLED_STR = "filled"
    ORDER_STATE_CANCELED_STR = "canceled"
    ORDER_STATE_PENDING_CANCEL_STR = "pending_cancel"
    ORDER_STATE_SYS_CANCELED_STR = "sys_canceled"
    ORDER_STATE_OPEN = (ORDER_STATE_PENDING_SUBMIT_STR, ORDER_STATE_SUBMITTED_STR, ORDER_STATE_PARTIAL_FILLED_STR,
                        ORDER_STATE_PENDING_CANCEL_STR)
    ORDER_STATE_CLOSED = (ORDER_STATE_PARTIAL_CANCELED_STR, ORDER_STATE_FILLED_STR,
                          ORDER_STATE_CANCELED_STR, ORDER_STATE_SYS_CANCELED_STR)


class Side(object):
    BUY = 0
    SELL = 1
    BUY_STR = "buy"
    SELL_STR = "sell"

    NAMES = (BUY_STR, SELL_STR)
    VALUES = (BUY, SELL)
    MAP = {name: value for name, value in zip(NAMES, VALUES)}
    MAP.update({name: value for name, value in zip(VALUES, NAMES)})
    # Buy: Open long/Close Short
    # Sell: Close Long/Open Short


class StopType(object):
    """
    trigger order
    1: greater than or equal to the trigger price
    2: less than or equal to the trigger price
    """
    NONE = 0  # None stop type
    GREATER_OR_EQUAL = 1  # >=
    LESS_OR_EQUAL = 2  # <=


class Direction(object):
    """
    Position direction
    """
    LONG = 0  # direction_long
    SHORT = 1  # direction_short
    LONG_STR = "long"
    SHORT_STR = "short"
    DIRECTION_LIST = (LONG, SHORT)
    DIRECTION_MAP = {LONG: LONG_STR,
                     SHORT: SHORT_STR,
                     LONG_STR: LONG,
                     SHORT_STR: SHORT}
    DIRECTION_INT_TO_STR_MAP = {LONG: LONG_STR,
                                SHORT: SHORT_STR}


class SwapTradeType(object):
    OPEN_LONG = 0x00
    CLOSE_LONG = 0x01
    OPEN_SHORT = 0x02
    CLOSE_SHORT = 0x03

    OPEN_LONG_STR = "openlong"  # buy
    CLOSE_LONG_STR = "closelong"  # sell
    OPEN_SHORT_STR = "openshort"  # sell
    CLOSE_SHORT_STR = "closeshort"  # buy

    LONG_TYPE = (OPEN_LONG, CLOSE_LONG)
    SHORT_TYPE = (OPEN_SHORT, CLOSE_SHORT)
    LONG_TYPE_STR = (OPEN_LONG_STR, CLOSE_LONG_STR)
    SHORT_TYPE_STR = (OPEN_SHORT_STR, CLOSE_SHORT_STR)

    OPEN_TYPE = (OPEN_LONG, OPEN_SHORT)
    CLOSE_TYPE = (CLOSE_LONG, CLOSE_SHORT)

    BUY_TYPE = (OPEN_LONG, CLOSE_SHORT)
    SELL_TYPE = (CLOSE_LONG, OPEN_SHORT)

    TYPE_LIST = (OPEN_LONG, CLOSE_LONG, OPEN_SHORT, CLOSE_SHORT)
    TYPE_LIST_STR = (OPEN_LONG_STR, CLOSE_LONG_STR, OPEN_SHORT_STR, CLOSE_SHORT_STR)
    CLOSE_TYPE_STR = (CLOSE_LONG_STR, CLOSE_SHORT_STR)
    OPEN_TYPE_STR = (OPEN_LONG_STR, OPEN_SHORT_STR)

    TYPE_MAP = {OPEN_LONG: OPEN_LONG_STR,
                CLOSE_LONG: CLOSE_LONG_STR,
                OPEN_SHORT: OPEN_SHORT_STR,
                CLOSE_SHORT: CLOSE_SHORT_STR,

                OPEN_LONG_STR: OPEN_LONG,
                CLOSE_LONG_STR: CLOSE_LONG,
                OPEN_SHORT_STR: OPEN_SHORT,
                CLOSE_SHORT_STR: CLOSE_SHORT,
                }

    SIDE_MAP = {OPEN_LONG: Side.BUY_STR,
                CLOSE_SHORT: Side.BUY_STR,
                CLOSE_LONG: Side.SELL_STR,
                OPEN_SHORT: Side.SELL_STR,
                }
    SIDE_STR_MAP = {OPEN_LONG_STR: Side.BUY_STR,
                    CLOSE_SHORT_STR: Side.BUY_STR,
                    CLOSE_LONG_STR: Side.SELL_STR,
                    OPEN_SHORT_STR: Side.SELL_STR,
                    }

    TO_DIRECTION_MAP = {OPEN_LONG_STR: Direction.LONG,
                        CLOSE_LONG_STR: Direction.LONG,
                        OPEN_SHORT_STR: Direction.SHORT,
                        CLOSE_SHORT_STR: Direction.SHORT,

                        OPEN_LONG: Direction.LONG,
                        CLOSE_LONG: Direction.LONG,
                        OPEN_SHORT: Direction.SHORT,
                        CLOSE_SHORT: Direction.SHORT,
                        }


class MarketType(object):
    LIMIT = 0
    MARKET = 1
    POST_ONLY = 2
    FOK = 3  # Fill Or Kill
    IOC = 4  # Immediate Or Cancel
    FAK = 5  # Fill And Kill

    LIMIT_STR = "limit"
    MARKET_STR = "market"

    LIST_INT = (LIMIT, MARKET)
    LIST_STR = (LIMIT_STR, MARKET_STR)

    MAP = {LIMIT: LIMIT_STR,
           MARKET: MARKET_STR,
           LIMIT_STR: LIMIT,
           MARKET_STR: MARKET}


class TriggerType(object):
    # trade while the price greater than trigger price
    TYPE_HIGHER = 0
    # trade while the price less than trigger price
    TYPE_LOWER = 1

    TYPE_LIST = (TYPE_HIGHER, TYPE_LOWER)


class AlgoOrderType(object):
    NONE = 0
    TRIGGER_ORDER = 1  # stop profit, stop loss
