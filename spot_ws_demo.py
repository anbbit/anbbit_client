import asyncio
import json

from clients.utils import run_sync
from clients.ws_client import AnbbitWsClient
from clients.constants import WsConf, ANBBIT_SPOT_WS_HOST


class AnbbitSpotWsClientDemo(AnbbitWsClient):

    async def on_message(self, data):
        print(f'on_message={data}')
        await self.dispatch(data)

    async def on_connected(self):
        print('connected success')

    async def dispatch(self, msg: str):
        if msg in (WsConf.PONG_RES, WsConf.WELLCOME):
            return

        msg = json.loads(msg)
        _type = msg['stream']
        print(f"type={_type}")

    async def sub_chan(self, sub_id, chan_list: list):
        sub_msg = {
            "method": "SUBSCRIBE",
            "params": chan_list,
            "id": sub_id
        }
        print(f"sub_msg={sub_msg}")
        await self.send(sub_msg)

    async def unsub_chan(self, sub_id, chan_list: list):
        sub_msg = {
            "method": "UNSUBSCRIBE",
            "params": chan_list,
            "id": sub_id
        }
        print(f"sub_msg={sub_msg}")
        await self.send(sub_msg)


async def main_single_sub():
    sub_url = ANBBIT_SPOT_WS_HOST
    timeout_sec = 60
    client = AnbbitSpotWsClientDemo(sub_url, timeout_sec)

    await asyncio.sleep(5)

    sub_id = 1
    symbol = 'btcusdt'
    kline_interval = '1m'
    chan_list = [
        # f'{symbol}@aggTrade',
        # f'{symbol}@depth',
        # f'{symbol}@kline_{kline_interval}',
        f'!miniTicker@arr',
    ]
    await client.sub_chan(sub_id=sub_id, chan_list=chan_list)


def test():
    run_sync(main_single_sub())
    loop = asyncio.get_event_loop()
    loop.run_forever()


if __name__ == "__main__":
    test()
