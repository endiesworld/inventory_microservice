import uuid
from typing import List, Optional

from fastapi import APIRouter, Depends, Request, status


from app.models.exceptions.crud_exception import DuplicateDataError, NotFoundError

router = APIRouter()
router.prefix = "/api/payment"

# platform_user = global_state.system_users.current_user(active=True, verified=True)


@router.get(
    "",
    tags=["payment-services"],
    name="payment:list",
    operation_id="payment_list",
    responses={
        status.HTTP_200_OK,
    },
)
async def list_payment(
    request: Request,
    name: Optional[str] = None,
):
    """
    """
    return {"response": "OK",
            "data": "To be provided soon"}

