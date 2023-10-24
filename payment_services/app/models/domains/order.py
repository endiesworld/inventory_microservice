from enum import Enum

from redis_om import HashModel, get_redis_connection

from pydantic import BaseModel
from app.core.global_config import app_config

# Get a Redis connection
db_host, db_port = (app_config.REDIS_CONTAINER_NAME, app_config.REDIS_PORT)
database = get_redis_connection(host=db_host, port=db_port, decode_responses=True)


class PaymentStatusEnum(str, Enum):
    pending = "pending"
    completed = "completed"
    refunded = "refunded"
    
    
class NewOrder(BaseModel):
    product_id: str
    product_name: str
    price: float
    commission: float
    total: float
    quantity: int
    status: PaymentStatusEnum
        
    
class NewOrderModel(HashModel):
    product_id: str
    product_name: str
    price: float
    commission: float
    total: float
    quantity: int
    status: PaymentStatusEnum
        
    class Meta:
            database = database


class OrderModel(NewOrder):
    id: str
    
