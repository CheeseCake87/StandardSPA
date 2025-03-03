from app import logger

from app.websockets.connection_handler import ConnectionHandler


async def print_connections(connection: ConnectionHandler, connections: set = None):
    _ = connection
    logger.info(f"print_connections: {connections}")
