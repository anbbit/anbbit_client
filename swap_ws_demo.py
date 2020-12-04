import asyncio
import gzip
import json

from clients.utils import get_cur_time_secs, run_sync
from clients.ws_client import AnbbitWsClient
from clients.constants import WsConf, ANBBIT_SWAP_WS_HOST


class AnbbitSwapWsClientDemo(AnbbitWsClient):
    @staticmethod
    def inflate(data):
        return gzip.decompress(data).decode('utf-8')

    async def on_message(self, data):
        msg = self.inflate(data)
        print(f'on_message={msg}')
        await self.dispatch(msg)

    async def on_connected(self):
        print('connected success')

    async def dispatch(self, msg: str):
        if msg in (WsConf.PONG_RES, WsConf.WELLCOME):
            return

        msg = json.loads(msg)
        _type = None
        if 'type' in msg:
            _type = msg['type']
        elif 'id' in msg:
            # kline
            _type = msg['id']
        print(f"type={_type}")

    async def sub_chan(self, chan_id):
        sub_msg = {'type': "sub",
                   'chan': chan_id,
                   'id': get_cur_time_secs(),
                   }
        print(f"sub_msg={sub_msg}")
        await self.send(sub_msg)

    async def unsub_chan(self, chan_id):
        sub_msg = {'type': "unsub",
                   'chan': chan_id,
                   'id': get_cur_time_secs(),
                   }
        print(f"sub_msg={sub_msg}")
        await self.send(sub_msg)


async def main_single_sub():
    symbol = 'BTC_USDT_P'
    # symbol = 'ETH_USDT_P'

    sub_url = ANBBIT_SWAP_WS_HOST
    timeout_sec = 60
    client = AnbbitSwapWsClientDemo(sub_url, timeout_sec)

    await asyncio.sleep(5)

    chan_id = WsConf.CHAN_TRADE.format(symbol=symbol)
    await client.sub_chan(chan_id=chan_id)
    # await client.unsub_chan(chan_id=chan_id)

    level = 'L50'
    chan_id = WsConf.CHAN_ORDERBOOK.format(symbol=symbol, level=level)
    await client.sub_chan(chan_id=chan_id)
    # await client.unsub_chan(chan_id=chan_id)

    chan_id = WsConf.CHAN_TICKER.format(symbol=symbol)
    await client.sub_chan(chan_id=chan_id)
    # await client.unsub_chan(chan_id=chan_id)

    kline_interval_1m = WsConf.KLINE_INTERVAL_1M
    chan_id_1m = WsConf.CHAN_KLINE.format(symbol=symbol, kline_interval=kline_interval_1m)
    await client.sub_chan(chan_id=chan_id_1m)
    # await client.unsub_chan(chan_id=chan_id)

    # kline_interval_3m = WsConf.KLINE_INTERVAL_3M
    # chan_id_3m = WsConf.CHAN_KLINE.format(symbol=symbol, kline_interval=kline_interval_3m)
    # await client.sub_chan(chan_id=chan_id_3m)
    # await client.unsub_chan(chan_id=chan_id)


def test():
    run_sync(main_single_sub())
    loop = asyncio.get_event_loop()
    loop.run_forever()


if __name__ == "__main__":
    test()
