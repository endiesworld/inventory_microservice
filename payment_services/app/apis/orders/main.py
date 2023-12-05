
import time
from typing import Optional, List
import requests

from fastapi.background import BackgroundTasks

from app.models.domains.order import (
    OrderModel, 
    NewOrderModel, 
    PaymentStatusEnum, 
    COMMISSION, 
    PRICE_FACTOR
)
from app.models.core import DeletedCount
from app.db.repositories import OrdersRepository

from . import crud



async def fn_create_order(
    product_id: str,
    quantity: int,
    order_repo: OrdersRepository,
    background_task: BackgroundTasks,
) -> Optional[OrderModel]:
    
    id = product_id
    
    response =  requests.get(f"http://inventory-services-backend:5000/api/inventory/products/{id}")
    
    if response.status_code == 200:
        product = response.json()
        new_order = NewOrderModel(
        product_id=id,
        product_name=product['name'],
        price=product['price'],
        commission=COMMISSION*product['price'],
        total=PRICE_FACTOR*product['price'],
        quantity=product['quantity'],
        status=PaymentStatusEnum.pending,
    )
        order_model, order = await crud.fn_create_order(new_order, order_repo)
        
        background_task.add_task(complete_order, order, order_repo)
        
        return order_model
    
    else:
        return {"error": "Failed to fetch data from the API"}
    


async def complete_order(order: NewOrderModel, order_repo:OrdersRepository):
    time.sleep(5)
    order.status = PaymentStatusEnum.completed
    await crud.fn_create_order(order, order_repo)
    
    
async def fn_get_order_by_id(
    order_id: str,
    order_repo: OrdersRepository,
) -> Optional[OrderModel]:
    
    return await crud.fn_get_order_by_id(order_id, order_repo)