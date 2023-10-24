from typing import List, Optional

from redis_om import NotFoundError

from app.db.base import BaseRepository
from app.models.domains.order import NewOrderModel, OrderModel

from app.models.exceptions.crud_exception import NotFoundException
from app.models.core import DeletedCount


class OrdersRepository(BaseRepository):
    async def create_order(self, *, new_order: NewOrderModel)-> Optional[OrderModel]:
        order = new_order.save()
        return OrderModel(
            id=order.pk,
            product_id=order.product_id,
            product_name=order.product_name,
            price=order.price,
            commission=order.commission,
            total=order.total,
            quantity=order.quantity,
            status=order.status,
        )
