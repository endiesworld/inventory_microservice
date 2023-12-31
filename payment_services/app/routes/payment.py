from typing import List, Optional, Any

from fastapi import APIRouter, Depends, Request, status
from fastapi.background import BackgroundTasks

from app.apis.orders import (
    fn_create_order, 
    fn_get_order_by_id
)

from app.models.domains.order import NewOrder, OrderModel
from app.models.exceptions.crud_exception import DuplicateDataError
from app.models.core import DeletedCount
from app.db.dependency import get_repository
from app.db.repositories import OrdersRepository

router = APIRouter()
router.prefix = "/api/payment"


# @router.get(
#     "/products",
#     tags=["payment-services"],
#     name="payment:list:products",
#     operation_id="payment_list_all_products",
#     status_code=status.HTTP_200_OK,
# )
# async def get_products(
#     request: Request,
#     product_repo: ProductsRepository= Depends(
#         get_repository(ProductsRepository)
#     )
#     )-> Optional[List[Product]]:
#     """
#         Get all products in the payment.
#     """
#     result = await fn_get_products(product_repo)
    
#     return result


@router.post(
    "/orders",
    tags=["payment-services"],
    name="payment:list",
    operation_id="payment_list",
    responses={status.HTTP_201_CREATED: {"model": OrderModel}},
    status_code=status.HTTP_201_CREATED,
)
async def create_order(
    request: Request,
    background_task: BackgroundTasks,
    product_id: str,
    quantity: int,
    order_repo: OrdersRepository= Depends(
        get_repository(OrdersRepository)
    ),
    )->Optional[OrderModel]:
    """
        Create new order.
    """
    return await fn_create_order(product_id, quantity, order_repo, background_task)


@router.get(
    "/orders/{order_id}",
    tags=["payment-services"],
    name="payment:unique:order",
    operation_id="payment_order_by_id",
    status_code=status.HTTP_200_OK,
)
async def get_order_by_id(
    request: Request,
    order_id: str,
    order_repo: OrdersRepository= Depends(
        get_repository(OrdersRepository)
    ),
    )-> Optional[OrderModel]:
    """
        Get a order by id.
    """
    result, _ = await fn_get_order_by_id(order_id, order_repo)
    
    return result


# @router.delete(
#     "/products/{id}",
#     tags=["payment-services"],
#     name="payment:unique:product:delete",
#     operation_id="delete_payment_product_by_id",
#     status_code=status.HTTP_200_OK,
# )
# async def delete_product_by_id(
#     request: Request,
#     id: str,
#     product_repo: ProductsRepository= Depends(
#         get_repository(ProductsRepository)
#     )
#     )-> Optional[DeletedCount]:
#     """
#         Delete a product from the payment by id.
#     """
    
#     return await fn_delete_product_by_id(id, product_repo)
    