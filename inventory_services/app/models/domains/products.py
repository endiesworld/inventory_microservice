from redis_om import HashModel, get_redis_connection

from pydantic import BaseModel
from app.core.global_config import app_config

# Get a Redis connection
db_host, db_port = (app_config.REDIS_CONTAINER_NAME, app_config.REDIS_PORT)
database = get_redis_connection(host=db_host, port=db_port, decode_responses=True)


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



