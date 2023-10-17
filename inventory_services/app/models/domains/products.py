from enum import Enum
from typing import List, Optional

from fastapi import Request
from app.models.core import CoreModel
from redis_om import HashModel



class NewProduct(HashModel):
    name: str
    price: float
    quantity: int
        
    class Meta:
        def __init__(self, request: Request):
            database = request.state.db


class Product():
    ...

