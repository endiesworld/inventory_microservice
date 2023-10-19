import uuid
from typing import List, Optional

from fastapi import APIRouter, Depends, Request, status

from app.apis.products import fn_create_product, fn_get_products

from app.models.domains.products import NewProduct, Product
from app.models.exceptions.crud_exception import DuplicateDataError, NotFoundError
from app.db.dependency import get_repository
from app.db.repositories import ProductsRepository

router = APIRouter()
router.prefix = "/api/inventory"


@router.get(
    "/products",
    tags=["Inventory-services"],
    name="inventory:list:products",
    operation_id="inventory_list_all_products",
    status_code=status.HTTP_200_OK,
)
async def get_products(
    request: Request,
    product_repo: ProductsRepository= Depends(
        get_repository(ProductsRepository)
    )
    ):
    """
        Get all products in the inventory.
    """
    result = await fn_get_products(product_repo)
    
    return result


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
    request: Request,
    new_product: NewProduct,
    product_repo: ProductsRepository= Depends(
        get_repository(ProductsRepository)
    ),
    )->Optional[Product]:
    """
        Add new product in the inventory.
    """
    return await fn_create_product(new_product, product_repo)

