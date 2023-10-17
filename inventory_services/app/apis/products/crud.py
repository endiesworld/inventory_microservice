from typing import Optional

from app.models.domains.products import NewProduct, Product
from app.db.repositories import ProductsRepository
from fastapi import Request

async def fn_create_product(
    new_product: NewProduct,
    product_repo: ProductsRepository,
    request: Request
) -> Optional[Product]:

    return await product_repo.create_product(new_product=new_product, request=request)