import uuid
from typing import List, Optional

from fastapi import APIRouter, Depends, Request, status


from app.models.exceptions.crud_exception import DuplicateDataError, NotFoundError

router = APIRouter()
router.prefix = "/api/inventory"

# platform_user = global_state.system_users.current_user(active=True, verified=True)


@router.get(
    "/",
    tags=["Inventory-services"],
    name="inventory:list",
    operation_id="inventory_list"
)
async def list_(request: Request,):
    return {"response": "OK",
            "data": "To be provided soon"}

