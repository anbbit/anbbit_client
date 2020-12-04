# -*- coding: utf-8 -*-

from clients.constants import WsConf
from clients.swap_market_client import AnbbitSwapMarketClient
from clients.utils import get_cur_time_secs


def test_swap_market():
    symbol = 'BTC_USDT_P'
    # symbol = 'ETH_USDT_P'

    swap_market_client = AnbbitSwapMarketClient()

    result = swap_market_client.market_orderbook(symbol=symbol)
    print(f'market_orderbook, result={result}')

    result = swap_market_client.market_trade(symbol=symbol)
    print(f'market_trade, result={result}')

    result = swap_market_client.market_ticker(symbol=symbol)
    print(f'market_ticker, result={result}')

    kline_interval = WsConf.KLINE_INTERVAL_1M
    end_tm = get_cur_time_secs()
    begin_tm = end_tm - 86400
    result = swap_market_client.market_kline(symbol=symbol, interval=kline_interval,
                                             begin_tm=begin_tm, end_tm=end_tm)
    print(f'market_kline, result={result}')


if __name__ == '__main__':
    test_swap_market()
