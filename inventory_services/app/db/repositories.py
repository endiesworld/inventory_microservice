from typing import List, Optional
from fastapi import Request

from app.models.domains.products import NewProduct, Product


class ProductsRepository():
    async def create_product(self, *, new_product: NewProduct, request: Request):
        ...