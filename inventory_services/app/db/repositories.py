from typing import List, Optional

from redis_om import NotFoundError

from app.db.base import BaseRepository
from app.models.domains.products import NewProductModel, Product

from app.models.exceptions.crud_exception import NotFoundException
from app.models.core import DeletedCount


class ProductsRepository(BaseRepository):
    async def create_product(self, *, new_product: NewProductModel)-> Optional[Product]:
        product = new_product.save()
        return Product(
            id=product.pk,
            name=product.name,
            price=product.price,
            quantity=product.quantity,
        )
    
    def get_product_by_id(self, id: str)-> List[Product]:
        try:
            product =  NewProductModel.get(id)
        except NotFoundError:
            raise NotFoundException(message="Sorry, no product with this Id was found.")
        
        product_ = Product(
            id=product.pk,
            name=product.name,
            price=product.price,
            quantity=product.quantity,
        )
        
        return (product_ , product)
        
    async def get_products(self):
        product_pks = NewProductModel.all_pks()
        product_list = []
        for pk in product_pks:
            product, _ = self.get_product_by_id(id=pk) 
            product_list.append( product)
        return product_list
    
    def delete_product_by_id(self, id:str)->Optional[DeletedCount]:
        deleted = NewProductModel.delete(id)
        return DeletedCount(count=deleted)