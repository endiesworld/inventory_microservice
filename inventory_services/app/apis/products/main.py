
from typing import Optional

from app.models.domains.products import NewProduct, Product
from app.db.repositories import ProductsRepository
from fastapi import Request

from . import crud

async def fn_create_product(
    new_product: NewProduct,
    product_repo: ProductsRepository,
    request: Request
) -> Optional[Product]:

    return await crud.fn_create_product(new_product, product_repo, request)
    