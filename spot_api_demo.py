from clients.constants import Side, MarketType
from clients.spot_api_client import AnbbitSpotClient
from config import API_KEY, API_SECRET


def test_spot():
    symbol = 'BTC_USDT'

    spot_client = AnbbitSpotClient(api_key=API_KEY, api_secret=API_SECRET)

    data = spot_client.signature_test()
    print("signature_test result=", data['auth'])

    res = spot_client.get_balance()
    print({'get_balance': res})

    res = spot_client.list_balance()
    print({'list_balance': res})

    # params = {
    #     'symbol': symbol,
    #     'side': Side.SELL_STR,
    #     'qty': 0.000998,
    #     'price': 19000,
    #     '_type': MarketType.LIMIT_STR,
    # }
    # res = spot_client.create_order(**params)
    # print({'create_order': res})

    # order_id = '3867330124'
    # res = spot_client.get_order_state(order_id=order_id, symbol=symbol)
    # print({'get_order_state': res})

    # order_id = '3867330124'
    # res = spot_client.cancel_order(order_id=order_id, symbol=symbol)
    # print({'cancel_order': res})

    # res = spot_client.list_active_order(symbol)
    # print({'list_active_order': res})

    # res = spot_client.list_history_order(symbol)
    # print({'list_history_order': res})

    # res = spot_client.list_trade(symbol)
    # print({'list_trade': res})

    res = spot_client.get_timestamp_ms()
    print({'get_timestamp_ms': res})

    # res = spot_client.list_symbol()
    # print({'list_symbol': res})

    # res = spot_client.list_currency()
    # print({'list_currency': res})

    # symbol_index = 'PT05_USDT'
    # res = spot_client.get_index_price(symbol=symbol_index)
    # print({'get_index_price': res})


if __name__ == '__main__':
    test_spot()
