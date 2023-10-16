import uuid
from typing import List, Optional

from fastapi import APIRouter, Depends, Request, status


from app.models.exceptions.crud_exception import DuplicateDataError, NotFoundError

router = APIRouter()
router.prefix = "/api/payment"


@router.get(
    "/",
    tags=["payment-services"],
    name="payment:list",
    operation_id="payment_list",
)
async def list_payment(
    request: Request,
    name: Optional[str] = None,
):
    """
        This spot is to be used for comments and description.
    """
    return {
        "response": "OK",
        "data": "To be provided soon"
        }
    

@router.put(
    "/",
    tags=["payment-services"],
    name="payment:list",
    operation_id="payment_list",
    
)
async def payment(
    request: Request,
    name: Optional[str] = None,
):
    """
        This spot is to be used for comments and description.
    """
    return {
        "response": "OK",
        "data": "To be provided soon"
        }

