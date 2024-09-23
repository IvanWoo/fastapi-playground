from fastapi import HTTPException, status, Request, FastAPI
from fastapi.responses import JSONResponse


class FastApiPlaygroundException(Exception):
    ...


class DuplicateNameError(FastApiPlaygroundException):
    """the name is duplicate"""


class InvalidNameError(FastApiPlaygroundException):
    """the name is invalid"""


def duplicate_name_error_handler(request: Request, exc: DuplicateNameError):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT, content={"message": "duplicate name"}
    )


def invalid_name_error_handler(request: Request, exc: InvalidNameError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST, content={"message": "invalid name"}
    )


_registered_exception_handlers = (
    (DuplicateNameError, duplicate_name_error_handler),
    (InvalidNameError, invalid_name_error_handler),
)


def register_exception_handlers(app: FastAPI) -> None:
    for err, handler in _registered_exception_handlers:
        app.add_exception_handler(err, handler)
