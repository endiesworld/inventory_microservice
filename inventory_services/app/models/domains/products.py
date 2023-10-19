from enum import Enum
import redis
from typing import List, Optional

from fastapi import Request
from app.models.core import CoreModel
from redis_om import HashModel

from pydantic import BaseModel
from app.core.global_config import app_config


db_host, db_port = (app_config.REDIS_CONTAINER_NAME, app_config.REDIS_PORT)
# Get a Redis connection
database = redis.StrictRedis(host=db_host, port=db_port, decode_responses=True)


class NewProduct(BaseModel):
    name: str
    price: float
    quantity: int
        
class Product(NewProduct):
    id: str
    
class NewProductModel(HashModel):
    name: str
    price: float
    quantity: int
        
    class Meta:
            database = database


# class ProductModel(BaseModel):
#     ...

