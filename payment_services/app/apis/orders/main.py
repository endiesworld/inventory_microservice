
from typing import Optional, List
import requests

from app.models.domains.order import (
    NewOrder, 
    RedisOrderModel,
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
    order_repo: OrdersRepository,
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
        order = await crud.fn_create_order(new_order, order_repo)
        
        order = RedisOrderModel(
            id=order.id,
            product_id=order.product_id,
            product_name=order.product_name,
            price=order.price,
            commission=order.commission,
            total=order.total,
            quantity=order.quantity,
            status=order.status
        )
        
        order = await complete_order(order, order_repo)
        return order
    
    else:
        return {"error": "Failed to fetch data from the API"}
    


async def complete_order(order: RedisOrderModel, order_repo:OrdersRepository)->OrderModel:
    order.status = PaymentStatusEnum.completed
    return await crud.fn_create_order(order, order_repo)
    
    