from typing import Callable
import asyncio
from fastapi import FastAPI

from app.events.consumer import process_redis_stream

def create_start_app_handler(app: FastAPI) -> Callable:
    from app.db import connect_to_db

    async def start_app() -> None:
        await connect_to_db(app)

    return start_app


def create_redis_refund_consumer():
    asyncio.create_task(process_redis_stream())

# def create_stop_app_handler(app: FastAPI) -> Callable:
#     from app.db import close_db_connection

#     async def stop_app() -> None:
#         await close_db_connection(app)

#     return stop_app