import asyncio

from app.websockets.server import WebsocketServer

server = WebsocketServer(
    host='127.0.0.1',
    port=5003
)

if __name__ == '__main__':
    asyncio.run(server.run())
