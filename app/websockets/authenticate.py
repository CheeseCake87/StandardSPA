from typing import Any

import orjson
from websockets.asyncio.server import ServerConnection

from app import logger


async def authenticate(
        payload: dict[str, Any],
        websocket: ServerConnection
):
    if "_key" not in payload:
        logger.error("No key provided")
        await websocket.send(
            orjson.dumps({"error": "No key provided"}),
            text=True
        )
        await websocket.close()
