import typing as t

import orjson
from websockets import exceptions
from websockets.asyncio.server import ServerConnection
from websockets.asyncio.server import serve

from app import logger
from app.websockets.actions import action_router
from app.websockets.authenticate import authenticate


class WebsocketServer:
    host: str = "120.0.0.1"
    port: int = 5003
    connections: t.Set = set()

    def __init__(self, host: str = "120.0.0.1", port: int = 5003):
        self.host = host
        self.port = port

    async def handler(self, websocket: ServerConnection):

        logger.info(f"Incoming connection - {websocket}")

        if websocket not in self.connections:
            self.connections.add(websocket)

            logger.info("New connection stored")

        logger.info("Connection established")

        try:

            # Wait for message to come in from connection above
            inbound_msg = await websocket.recv()

            try:

                payload = orjson.loads(inbound_msg)

                # Will look for a key called _key and validate
                # it towards the database. Will close the connection if not valid
                await authenticate(payload=payload, websocket=websocket)

                await websocket.send(
                    orjson.dumps({"info": "Connection authenticated"}),
                    text=True
                )

                # Looks for a key called _action and directs the request to
                # other internal code.
                await action_router(payload=payload, websocket=websocket)

            except orjson.JSONDecodeError:

                logger.error(f"Invalid JSON message: {inbound_msg}")

                await websocket.send(orjson.dumps({"error": "Invalid Message"}))
                return

                # Loop back to handler
            await self.handler(websocket)

        except exceptions.ConnectionClosedError:
            logger.error("Connection closed error")
            pass

        except exceptions.ConnectionClosedOK:
            logger.info("Connection closed OK")
            pass

        finally:
            if websocket in self.connections:
                logger.info(f"Removing connection: {websocket}")
                self.connections.remove(websocket)

    async def run(self):
        logger.info("Starting websocket server...")

        async with serve(self.handler, self.host, self.port) as server:
            logger.info(f"Websocket server running on {self.host}:{self.port}")
            await server.serve_forever()
