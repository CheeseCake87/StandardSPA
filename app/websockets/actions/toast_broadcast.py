from app import logger

from app.websockets.connection_handler import ConnectionHandler
from app.websockets.helpers import responder


async def toast_broadcast(connection: ConnectionHandler, connections: set = None):
    message = connection.data.get("message", "No toast message provided")

    logger.info(f"toast-broadcast: {message}")

    for con in connections:
        await responder(
            con,
            action="toast-broadcast",
            data={"message": message}
        )
