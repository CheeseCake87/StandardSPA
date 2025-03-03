import typing as t

from websockets import exceptions
from websockets.asyncio.server import ServerConnection
from websockets.asyncio.server import serve

from app import logger
from app.websockets.actions import authenticate, action_router
from app.websockets.connection_handler import ConnectionHandler


class WebsocketServer:
    host: str = "120.0.0.1"
    port: int = 5003
    connections: t.Set = set()

    def __init__(self, host: str = "120.0.0.1", port: int = 5003):
        self.host = host
        self.port = port

    async def handler(self, websocket: ServerConnection):

        id_ = websocket.id

        logger.info(f"Incoming connection - {id_}")

        if websocket not in self.connections:
            self.connections.add(websocket)

            logger.info("New connection stored")

        logger.info("Connection established")

        try:

            inbound_msg = await websocket.recv()
            connection = await ConnectionHandler(websocket).decode(inbound_msg)
            await authenticate(connection=connection)
            await action_router(connection=connection, connections=self.connections)

            await self.handler(websocket)

        except exceptions.ConnectionClosedError:
            logger.error("Connection closed error")
            pass

        except exceptions.ConnectionClosedOK:
            logger.info("Connection closed OK")
            pass

        finally:
            if websocket in self.connections:
                logger.info(f"Removing connection: {id_}")
                self.connections.remove(websocket)

    async def run(self):
        logger.info("Starting websocket server...")

        async with serve(self.handler, self.host, self.port) as server:
            logger.info(f"Websocket server running on {self.host}:{self.port}")
            await server.serve_forever()
