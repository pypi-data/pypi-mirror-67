from typing import Callable

from requests import Timeout
from telegrambotapiwrapper import Api


def _process_existing_updates(bot_api, handler):
    offset = None

    while True:
        existing_updates = bot_api.get_updates(offset=offset)
        if existing_updates:
            for update in existing_updates:
                handler(update)
                offset = update.update_id + 1
        else:
            return


def listen(token: str,
           handler: Callable,
           process_existing: bool = False,
           timeout: int = 20,
           ):
    bot_api = Api(token=token)
    if process_existing:
        _process_existing_updates(bot_api, handler)
    else:
        _process_existing_updates(bot_api, lambda update: None)

    offset = None
    while True:
        try:
            updates = bot_api.get_updates(offset=offset, timeout=timeout)
        except Timeout:
            continue
        for update in updates:
            handler(update)
            offset = update.update_id + 1
