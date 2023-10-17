import uuid
from typing import List, Optional

from fastapi import APIRouter, Depends, Request, status

from app.apis.products import fn_create_product

from app.models.domains.products import NewProduct, Product
from app.models.exceptions.crud_exception import DuplicateDataError, NotFoundError

from app.db.repositories import ProductsRepository

router = APIRouter()
router.prefix = "/api/inventory"

# platform_user = global_state.system_users.current_user(active=True, verified=True)


@router.get(
    "",
    tags=["Inventory-services"],
    name="inventory:list",
    operation_id="inventory_list"
)
async def list_(request: Request,name: Optional[str] = None,):
    return {"response": "OK",
            "data": "To be provided soon"}

@router.post(
    "",
    tags=["Inventory-services"],
    name="inventory:list",
    operation_id="inventory_list",
    responses={
        status.HTTP_201_CREATED: {"model": Product},
        status.HTTP_403_FORBIDDEN: {"model": DuplicateDataError},
    },
    status_code=status.HTTP_201_CREATED,
)
async def create_product(
    new_product: NewProduct,
    product_repo: ProductsRepository,
    request: Request):
    """
        This spot is to be used for comments and description.
    """
    return await fn_create_product(new_product, product_repo, request)

