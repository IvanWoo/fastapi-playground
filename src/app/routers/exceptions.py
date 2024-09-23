from fastapi import APIRouter
from app.exception_handlers import DuplicateNameError, InvalidNameError

router = APIRouter()

router = APIRouter(
    prefix="/exceptions",
    tags=["exceptions"],
    responses={404: {"description": "Not found"}},
)


@router.get("/duplicate_name")
async def raise_duplicate_name_error():
    raise DuplicateNameError()


@router.get("/invalid_name")
async def raise_invalid_name_error():
    raise InvalidNameError()
