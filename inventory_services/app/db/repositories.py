from typing import List, Optional

from fastapi import Request

from app.db.base import BaseRepository
from app.models.domains.products import NewProductModel, Product


class ProductsRepository(BaseRepository):
    async def create_product(self, *, new_product: NewProductModel, request: Request):
        return new_product.save()
        
    
    def get_products(self, *, request: Request):
        print(NewProductModel.all_pks())
        return [format(pk) for pk in NewProductModel.all_pks()]
    
    def format(pk: str):
        product = NewProductModel.get(pk)
        return {
            'id': product.pk,
            'name': product.name,
            'price': product.price,
            'quantity': product.quantity
        }