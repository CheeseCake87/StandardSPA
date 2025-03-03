from typing import Any

import orjson
from websockets.asyncio.server import ServerConnection


def encode(payload: dict[Any, str]):
    return orjson.dumps(payload)


async def responder(connection: ServerConnection, key: str = "-", action: str = "-", data: dict[str, Any] = None):
    if data is None:
        data = {}

    await connection.send(encode(
        {
            "key": key,
            "action": action,
            "data": data
        }
    ), text=True)
