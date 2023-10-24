from typing import Optional, List, Any

from app.models.domains.order import NewOrder, OrderModel, NewOrderModel
from app.db.repositories import OrdersRepository
from app.models.core import DeletedCount

async def fn_create_order(
    new_order: NewOrderModel,
    order_repo: OrdersRepository,
) -> Optional[OrderModel]:

    return await order_repo.create_order(new_order=new_order)

