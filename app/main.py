from fastapi import Depends, FastAPI

from app.dependencies import get_query_token, get_token_header
from app.internal import admin
from app.routers import items, users, notifications, exceptions
from app.exception_handlers import register_exception_handlers

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(users.router)
app.include_router(items.router)
app.include_router(notifications.router)
app.include_router(exceptions.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)
register_exception_handlers(app)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
