from typing import Any

import orjson
from websockets.asyncio.server import ServerConnection

from app import logger
from app.websockets.helpers import responder


class ConnectionHandler:
    websocket: ServerConnection
    connections: set

    incoming_msg: str | bytes

    key: str
    action: str
    data: dict[str, str]

    def __init__(self, websocket: ServerConnection, connections: set = None):
        self.websocket = websocket
        self.connections = connections if connections else set()
        self.key = ""
        self.action = ""
        self.data = {}

    async def decode(self, incoming_msg: str | bytes):
        self.incoming_msg = incoming_msg

        try:
            decoded = orjson.loads(incoming_msg)

            _key = decoded.get("key")
            _action = decoded.get("action")
            _data = decoded.get("data")

            if _key:
                self.key = _key
            if _action:
                self.action = _action
            if _data:
                self.data = _data

        except orjson.JSONDecodeError:
            logger.error(f"Invalid JSON message: {incoming_msg}")

            await self.respond({"error": "Invalid Message"})

        return self

    async def respond(self, data: dict[str, Any]):
        """
        Returns a response to the client with the key, action and data

        {
        "key": "some-key",
        "action": "some-action",
        "data": {...}
        }

        :param data:
        :return:
        """
        await responder(
            self.websocket,
            self.key,
            self.action,
            data
        )
