import asyncio
import typing as t

from websockets import exceptions
from websockets.asyncio.server import serve

from app.utilities.sys_print import sys_print_websockets


class WebsocketServer:
    host: str = "120.0.0.1"
    port: int = 5003
    connections: t.Set = set()
    authenticated: t.Set = set()
    lookup: t.Dict = dict()

    def __init__(self, host: str = "120.0.0.1", port: int = 5003):
        self.host = host
        self.port = port

    def set_lookup(self, websocket):
        self.lookup[websocket.id] = websocket

    async def handler(self, websocket):
        if websocket not in self.connections:
            self.connections.add(websocket)
            sys_print_websockets(
                ["Adding new connection", websocket.remote_address]
            )

        try:
            sys_print_websockets([
                f"Connection established: {websocket.remote_address[0]}:{websocket.remote_address[1]}",
                f"Connections: {self.connections}",
                f"Authenticated: {self.authenticated}",
                f"Lookup: {self.lookup}",
            ])

            # Wait for message to come in from connection above
            inbound_msg = await websocket.recv()

            sys_print_websockets([
                f"Inbound: {inbound_msg}",
                f"From {websocket.remote_address[0]}:{websocket.remote_address[1]}"
            ])

            # Loop back to handler
            await self.handler(websocket)

        except exceptions.ConnectionClosedError:
            sys_print_websockets([
                f"Connection closed on error: {websocket}"
            ])
            pass

        except exceptions.ConnectionClosedOK:
            sys_print_websockets([
                f"Connection closed on ok: {websocket}"
            ])
            pass

        finally:
            if websocket in self.connections:
                sys_print_websockets([
                    f"Removing {websocket} from connections"
                ])
                self.connections.remove(websocket)

    async def run(self):
        sys_print_websockets(["Starting websocket server..."])

        async with serve(self.handler, self.host, self.port):
            sys_print_websockets([
                f"Websocket server running on {self.host}:{self.port}"
            ])
            await asyncio.Future()
