from app import logger

from app.websockets.connection_handler import ConnectionHandler


async def toast(connection: ConnectionHandler):
    message = connection.data.get("message", "No toast message provided")

    logger.info(f"toast: {message}")

    await connection.respond({"message": message})
