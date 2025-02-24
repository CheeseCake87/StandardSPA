from typing import Any

import orjson
from websockets.asyncio.server import ServerConnection

from app import logger


async def action_router(
        payload: dict[str, Any],
        websocket: ServerConnection
):
    if "_action" not in payload:
        logger.error("No action provided")
        await websocket.send(
            orjson.dumps({"error": "No action provided"}),
            text=True
        )

    action = payload["_action"]
    data = payload.get("data", {})

    match action:
        case "echo":
            message = data.get("message", "No message provided")
            logger.info(f"Echoing message: {message}")
            await websocket.send(
                orjson.dumps({"echo": message}),
                text=True
            )
        case _:
            logger.error(f"Invalid action: {action}")
            await websocket.send(
                orjson.dumps({"error": "Invalid action"}),
                text=True
            )
