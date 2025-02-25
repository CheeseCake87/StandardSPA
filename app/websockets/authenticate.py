from app import logger
from app.websockets.connection_handler import ConnectionHandler


async def authenticate(connection: ConnectionHandler):
    if not connection.key:
        logger.error("No key provided")
        await connection.respond({"error": "No key provided"})
        await connection.websocket.close()

    await connection.respond({"info": "Connection authenticated"})
