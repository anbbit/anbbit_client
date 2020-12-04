import uuid
from clients.spot_api_client import AnbbitSpotClient
from config import API_KEY, API_SECRET


def test_spot():
    symbol = 'BTC_USDT'
    symbol = 'PT05_USDT'

    spot_client = AnbbitSpotClient(api_key=API_KEY, api_secret=API_SECRET)

    res = spot_client.get_timestamp_ms()
    print({'get_timestamp_ms': res})

    res = spot_client.list_symbol()
    print({'list_symbol': res})

    res = spot_client.list_currency()
    print({'list_currency': res})

    res = spot_client.get_index_price(symbol=symbol)
    print({'get_index_price': res})


if __name__ == '__main__':
    test_spot()
