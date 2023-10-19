from typing import Optional, List

from app.models.domains.products import Product, NewProductModel
from app.db.repositories import ProductsRepository
from fastapi import Request

async def fn_create_product(
    new_product: NewProductModel,
    product_repo: ProductsRepository,
) -> Optional[Product]:

    return await product_repo.create_product(new_product=new_product)

async def fn_get_products(product_repo: ProductsRepository)-> Optional[List[Product]]:
    
    return await product_repo.get_products()