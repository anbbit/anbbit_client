# -*- coding: utf-8 -*-

from clients.constants import WsConf
from clients.spot_market_client import AnbbitSpotMarketClient
from clients.utils import get_cur_time_ms


def test_spot_market():
    symbol = 'BTCUSDT'
    # symbol = 'ETHUSDT'

    spot_market_client = AnbbitSpotMarketClient()

    result = spot_market_client.market_orderbook(symbol=symbol)
    print(f'market_orderbook, result={result}')

    result = spot_market_client.market_aggregate_trade(symbol=symbol)
    print(f'market_aggregate_trade, result={result}')

    result = spot_market_client.market_ticker_24hr(symbol)
    print(f'market_ticker_24hr, result={result}')

    kline_interval = WsConf.KLINE_INTERVAL_1M
    # end_tm_ms = get_cur_time_ms()
    # start_tm_ms = end_tm - 86400000
    result = spot_market_client.market_kline(symbol=symbol, interval=kline_interval)
    print(f'market_kline, result={result}')


if __name__ == '__main__':
    test_spot_market()
