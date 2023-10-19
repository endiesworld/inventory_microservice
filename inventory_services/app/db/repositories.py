from typing import List, Optional

from app.db.base import BaseRepository
from app.models.domains.products import NewProductModel, Product


class ProductsRepository(BaseRepository):
    async def create_product(self, *, new_product: NewProductModel)-> Optional[Product]:
        product = new_product.save()
        return Product(
            id=product.pk,
            name=product.name,
            price=product.price,
            quantity=product.quantity,
        )
    
    def get_product_by_id(self, id: str)-> Product:
        product =  NewProductModel.get(id)
        product_ = Product(
            id=product.pk,
            name=product.name,
            price=product.price,
            quantity=product.quantity,
        )
        
        return product_
        
    async def get_products(self):
        product_pks = NewProductModel.all_pks()
        return [self.get_product_by_id(id=pk) for pk in product_pks]