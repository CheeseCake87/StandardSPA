from app import logger
from ..connection_handler import ConnectionHandler


async def authenticate(connection: ConnectionHandler):
    if not connection.key:
        logger.error("No key provided")
        await connection.respond({"error": "No key provided"})
        await connection.websocket.close()

    await connection.respond({"info": "Connection authenticated"})


async def action_router(connection: ConnectionHandler):
    if not connection.action:
        logger.error("No action provided")
        await connection.respond({"error": "No action provided"})

    match connection.action:
        case "echo":
            from .echo import echo
            await echo(connection)

        case _:
            logger.error(f"Invalid action: {connection.action}")
            await connection.respond({"error": "Invalid action"})
