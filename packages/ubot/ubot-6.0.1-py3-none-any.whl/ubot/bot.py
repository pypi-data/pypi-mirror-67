import asyncio
from typing import NamedTuple
from urllib.parse import urlencode

from ._utils.case_insensitive_dict import CaseInsensitiveDict
from ._utils.connection_pool import HttpConnectionPool


class BotRequest(NamedTuple):
    endpoint: str
    method: str = 'GET'
    params: dict = {}
    data: bytes = None
    headers: CaseInsensitiveDict = CaseInsensitiveDict()


class Bot:
    update_types = [
        ('message', 'message'),
        ('edited_message', 'message'),
        ('channel_post', 'message'),
        ('edited_channel_post', 'message'),
        ('inline_query', 'inline_query'),
        ('chosen_inline_result', 'chosen_inline_result'),
        ('callback_query', 'callback_query'),
        ('shipping_query', 'shipping_query'),
        ('pre_checkout_query', 'pre_checkout_query')
    ]

    # optional features
    check_update = None

    def __init__(self, token, *, loop=None, connection_pool_size=5):
        """
        The Class(TM).

        :param token: The Telegram-given token
        :param loop: The loop the bot is run into (if it's not asyncio.get_event_loop())
        """

        self.token = token

        if loop is None:
            self.loop = asyncio.get_event_loop()
        else:
            self.loop = loop

        self.base_path = f'bot{token}/'
        self.connection_pool = HttpConnectionPool('api.telegram.org', loop=loop, size=connection_pool_size)
        self.triggers = []
        self.update_queue = asyncio.PriorityQueue(loop=self.loop)

    async def api_request(self, request: BotRequest):
        """
        Makes a Telegram request with the params given in the BotRequest

        :param request: A BotRequest
        :return: The response from the server
        """

        endpoint = request.endpoint
        params = request.params
        data = request.data
        headers = request.headers

        if params:
            path = f'{self.base_path}{endpoint}?{urlencode(params)}'
        else:
            path = f'{self.base_path}{endpoint}'

        return await self.connection_pool.request(path=path, method=request.method, body=data, headers=headers)

    def get_type_and_flavor(self, update):
        for _type, flavor in self.update_types:
            if _type in update:
                update['_type'] = _type
                update['_flavor'] = flavor
                return
        else:
            update['_type'] = None
            update['_flavor'] = None

    async def start(self):
        """Main loop"""

        while True:
            _, update = await self.update_queue.get()
            self.loop.create_task(self.handle_update(update))

    async def handle_update(self, update):
        # check the update if the function is implemented and skip if it's not passed
        # note that while the function is called check_update it's basically a pre-processing hook, so if you have to
        # call get_type_and_flavor do it here
        check_update = self.check_update
        if check_update:
            is_check_passed = await check_update(update)
            if is_check_passed is not True:
                return

        for trigger in self.triggers:
            is_update_matched = await trigger.match(update, self)
            if is_update_matched:
                return await trigger.handle(update, self)

    def push_update(self, update):
        """
        Pushes an update (already json decoded) into the queue.

        :param update: The update to be pushed in the queue
        """

        self.update_queue.put_nowait((update['update_id'], update))

    def trigger(self, trigger):
        """
        Decorates a Trigger, inserting it into the bot check list
        """

        # maybe trigger may already be instances? Or we can call the methods directly?
        # or use factory methods
        self.triggers.append(trigger)
        return trigger
