from typing import List, Optional, Any

from fastapi import APIRouter, Depends, Request, status

from app.apis.products import (
    fn_create_product, 
    fn_get_products,
    fn_get_product_by_id,
    fn_delete_product_by_id
)

from app.models.domains.products import NewProduct, Product
from app.models.exceptions.crud_exception import DuplicateDataError
from app.models.core import DeletedCount
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
    )-> Optional[List[Product]]:
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


@router.get(
    "/products/{id}",
    tags=["Inventory-services"],
    name="inventory:unique:product",
    operation_id="inventory_product_by_id",
    status_code=status.HTTP_200_OK,
)
async def get_product_by_id(
    request: Request,
    id: str,
    product_repo: ProductsRepository= Depends(
        get_repository(ProductsRepository)
    )
    )-> Optional[Product]:
    """
        Get a product by id.
    """
    result = await fn_get_product_by_id(id, product_repo)
    
    return result


@router.delete(
    "/products/{id}",
    tags=["Inventory-services"],
    name="inventory:unique:product:delete",
    operation_id="delete_inventory_product_by_id",
    status_code=status.HTTP_200_OK,
)
async def delete_product_by_id(
    request: Request,
    id: str,
    product_repo: ProductsRepository= Depends(
        get_repository(ProductsRepository)
    )
    )-> Optional[DeletedCount]:
    """
        Delete a product from the inventory by id.
    """
    
    return await fn_delete_product_by_id(id, product_repo)
    