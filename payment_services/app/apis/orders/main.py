
from typing import Optional, List
import requests

from app.models.domains.order import NewOrder, OrderModel, NewOrderModel
from app.models.core import DeletedCount
from app.db.repositories import OrdersRepository

from . import crud

async def fn_create_order(
    new_order: NewOrder,
    order_repo: OrdersRepository,
) -> Optional[OrderModel]:
    
    id = new_order.product_id
    
    response =  requests.get(f"http://inventory-services-backend:5000/api/inventory/products/{id}")
    
    # new_order = NewOrderModel(
    #     product_id=new_order.product_id,
    #     product_name=new_order.product_name,
    #     price=new_order.price,
    #     commission=new_order.commission,
    #     total=new_order.total,
    #     quantity=new_order.quantity,
    #     status=new_order.status,
    # )
    # return await crud.fn_create_order(new_order, order_repo)
    if response.status_code == 200:
        data = response.json()
        print(f"RESPONSE: {response}")
        return {"data": data}
    else:
        return {"error": "Failed to fetch data from the API"}
    

