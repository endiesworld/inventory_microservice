from typing import Optional, List, Any

from app.models.domains.products import Product, NewProductModel
from app.db.repositories import ProductsRepository
from app.models.core import DeletedCount

async def fn_create_product(
    new_product: NewProductModel,
    product_repo: ProductsRepository,
) -> Optional[Product]:

    return await product_repo.create_product(new_product=new_product)

async def fn_get_products(product_repo: ProductsRepository)-> Optional[List[Product]]:
    
    return await product_repo.get_products()

async def fn_get_product_by_id(
    id: str,
    product_repo: ProductsRepository
)-> List[Product]:
    
    return  product_repo.get_product_by_id(id=id)

async def fn_delete_product_by_id(
    id: str,
    product_repo: ProductsRepository
)-> Optional[DeletedCount]:
    return  product_repo.delete_product_by_id(id=id)