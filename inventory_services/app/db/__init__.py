import os

from fastapi import FastAPI
from redis_om import HashModel, get_redis_connection
from loguru import logger

from app.core.global_config import app_config


async def connect_to_db(app: FastAPI) -> None:
    db_host, db_port = (app_config.REDIS_CONTAINER_NAME, app_config.REDIS_PORT)
   
    # Get a Redis connection
    database = get_redis_connection(host=db_host, port=db_port, decode_responses=True)
    
    # for creating a test database
    # if os.environ.get("TEST"):
    #     database_url += "_test"
    
    try:
        app.state.db = database
        logger.info(
            "--- DB CONNECTION ESTABLISHED TO {}---".format(app_config.REDIS_CONTAINER_NAME)
        )
    except Exception as e:
        logger.warning("--- DB CONNECTION ERROR ---")
        logger.warning(e)
        logger.warning("--- DB CONNECTION ERROR ---")


# async def close_db_connection(app: FastAPI) -> None:
#     try:
#         await app.state.db.disconnect()
#     except Exception as e:
#         logger.warning("--- DB DISCONNECT ERROR ---")
#         logger.warning(e)
#         logger.warning("--- DB DISCONNECT ERROR ---")
