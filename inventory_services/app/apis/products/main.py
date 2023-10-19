
from typing import Optional, List

from app.models.domains.products import NewProduct, Product, NewProductModel
from app.db.repositories import ProductsRepository
from fastapi import Request

from . import crud

async def fn_create_product(
    new_product: NewProduct,
    product_repo: ProductsRepository,
) -> Optional[Product]:
    
    new_product = NewProductModel(
        name = new_product.name,
        price = new_product.price,
        quantity = new_product.quantity
    )
    return await crud.fn_create_product(new_product, product_repo)

async def fn_get_products(product_repo: ProductsRepository)-> Optional[List[Product]]:
    
    return await crud.fn_get_products(product_repo)