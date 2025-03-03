from app import logger

from app.websockets.connection_handler import ConnectionHandler


async def echo(connection: ConnectionHandler):
    message = connection.data.get("message", "No message provided")

    logger.info(f"Echoing message: {message}")

    await connection.respond({"message": message})
