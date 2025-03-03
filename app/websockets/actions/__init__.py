from app import logger
from ..connection_handler import ConnectionHandler


async def authenticate(connection: ConnectionHandler):
    if not connection.key:
        logger.error("No key provided")
        await connection.respond({"error": "No key provided"})
        await connection.websocket.close()


async def action_router(connection: ConnectionHandler, connections: set = None):
    if not connection.action:
        logger.error("No action provided")
        await connection.respond({"error": "No action provided"})

    match connection.action:
        case "echo":
            from .echo import echo
            await echo(connection)

        case "toast":
            from .toast import toast
            await toast(connection)

        case "toast-broadcast":
            from .toast_broadcast import toast_broadcast
            await toast_broadcast(connection, connections)

        case "print-connections":
            from .print_connections import print_connections
            await print_connections(connection, connections)

        case _:
            logger.error(f"Invalid action: {connection.action}")
            await connection.respond({"error": "Invalid action"})
