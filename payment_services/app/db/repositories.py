from typing import List, Optional, Any

from redis_om import NotFoundError

from app.db.base import BaseRepository
from app.models.domains.order import NewOrderModel, OrderModel

from app.models.exceptions.crud_exception import NotFoundException


class OrdersRepository(BaseRepository):
    async def create_order(self, *, new_order: NewOrderModel)-> Any:
        order = new_order.save()
        order_model =  OrderModel(
            id=order.pk,
            product_id=order.product_id,
            product_name=order.product_name,
            price=order.price,
            commission=order.commission,
            total=order.total,
            quantity=order.quantity,
            status=order.status,
        )
        
        return (order_model, order)


    def get_order_by_id(self, id: str)-> List[OrderModel]:
        try:
            order =  NewOrderModel.get(id)
        except NotFoundError:
            raise NotFoundException(message="Sorry, no order with this Id was found.")
        
        order_ = OrderModel(
            id=order.pk,
            product_id=order.product_id,
            product_name=order.product_name,
            price=order.price,
            commission=order.commission,
            total=order.total,
            quantity=order.quantity,
            status=order.status,
        )
        
        return (order_, order)