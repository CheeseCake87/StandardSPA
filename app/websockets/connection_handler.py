from typing import Any

import orjson
from websockets.asyncio.server import ServerConnection

from app import logger


class ConnectionHandler:
    websocket: ServerConnection
    incoming_msg: str | bytes

    key: str
    action: str
    data: dict[str, str]

    def __init__(self, websocket: ServerConnection):
        self.websocket = websocket

    @staticmethod
    def encode(payload: dict[Any, str]):
        return orjson.dumps(payload)

    async def decode(self, incoming_msg: str | bytes):
        self.incoming_msg = incoming_msg

        try:
            decoded = orjson.loads(incoming_msg)

            self.key = decoded.get("key", "")
            self.action = decoded.get("action", "")
            self.data = decoded.get("data", {})

        except orjson.JSONDecodeError:
            logger.error(f"Invalid JSON message: {incoming_msg}")

            await self.respond({"error": "Invalid Message"})

        return self

    async def respond(self, payload: dict[str, Any]):
        await self.websocket.send(self.encode(payload), text=True)
