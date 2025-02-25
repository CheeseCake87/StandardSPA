from app import logger

from app.websockets.connection_handler import ConnectionHandler


async def echo(payload: ConnectionHandler):
    message = payload.data.get("message", "No message provided")

    logger.info(f"Echoing message: {message}")

    await payload.respond({"echo": message})
