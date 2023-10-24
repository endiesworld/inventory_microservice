
from typing import Optional, List

from app.models.domains.order import NewOrder, OrderModel, NewOrderModel
from app.models.core import DeletedCount
from app.db.repositories import OrdersRepository

from . import crud

async def fn_create_order(
    new_order: NewOrder,
    order_repo: OrdersRepository,
) -> Optional[OrderModel]:
    
    new_order = NewOrderModel(
        product_id=new_order.product_id,
        product_name=new_order.product_name,
        price=new_order.price,
        commission=new_order.commission,
        total=new_order.total,
        quantity=new_order.quantity,
        status=new_order.status,
    )
    return await crud.fn_create_product(new_order, order_repo)


