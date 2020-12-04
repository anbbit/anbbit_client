from uuid import uuid4
from clients.swap_api_client import AnbbitSwapClient
from config import API_KEY, API_SECRET


def test_swap():
    symbol = 'BTC_USDT_P'
    # symbol = 'ETH_USDT_P'

    swap_client = AnbbitSwapClient(api_key=API_KEY, api_secret=API_SECRET)

    # data = swap_client.signature_test()
    # print("signature_test result=", data['auth'])

    # res = swap_client.list_accounts()
    # print({'account_list': res})

    # res = swap_client.list_account_state(symbol=symbol)
    # print({'account_list': res})

    # res = swap_client.update_account_leverage(symbol=symbol, leverage=1, direction='long')  # long/short
    # print({'account_leverage': res})

    # res = swap_client.list_position(symbol=symbol)
    # print({'list_position': res})

    # qty = 0.001
    # price = 10000
    # trade_type = 'openlong'
    # _type = 'market'
    # amount = 100
    # res = swap_client.create_order(symbol, qty, price, trade_type, amount=amount, _type=_type)
    # print({'create_order': res})

    # orders = [
    #             {
    #                 'cid': f"cid_{uuid4().hex}",
    #                 "qty": 0.001,
    #                 "price": 10000,
    #                 "trade_type": "openlong",
    #                 'amount': 10,
    #                 'type': "market",  # limit/market
    #             },
    #         ]
    # res = swap_client.create_batch_order(symbol=symbol, orders=orders, account_type='swap')
    # print({'create_batch_order': res})

    # res = swap_client.list_order_state(symbol=symbol, order_id='3.BTC_USDT_P.0.f3c5c3ba08e40d17')
    # print({'list_order_state': res})

    # res = swap_client.cancel_order(symbol=symbol, order_id='3.BTC_USDT_P.0.f3c5c3ba08e40d17')
    # print({'cancel_order': res})

    # res = swap_client.cancel_all_order(symbol=symbol)
    # print({'cancel_all_order': res})

    # res = swap_client.cancel_batch_order(symbol=symbol, order_ids=['3.BTC_USDT_P.0.f3c5c3ba08e40d17'])
    # print({'cancel_batch_order': res})

    # res = swap_client.list_active_order(symbol=symbol)
    # print('list_active_order=', res)

    # res = swap_client.list_history_order(symbol=symbol)
    # print({'list_order_history': res})

    # res = swap_client.list_trade_list(symbol=symbol)
    # print({'trade_list': res})

    res = swap_client.list_balance(symbol=symbol)
    print({'test_balance': res})

    res = swap_client.list_balance_list()
    print({'balance_list': res})

    # res = swap_client.list_symbol()
    # print({'list_symbol': res})

    # res = swap_client.get_index_price(symbol=symbol)
    # print({'get_index_price': res})


if __name__ == '__main__':
    test_swap()
