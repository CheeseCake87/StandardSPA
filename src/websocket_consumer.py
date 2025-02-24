import asyncio

from app.websockets import server

if __name__ == '__main__':
    asyncio.run(server.run())
