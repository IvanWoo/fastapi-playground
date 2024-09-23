from fastapi import Depends, FastAPI

from app.dependencies import verify_query_token, authorized
from app.internal import admin
from app.routers import items, users, notifications, exceptions, queues, upload
from app.exception_handlers import register_exception_handlers
from app.config.lifespan import lifespan

app = FastAPI(title="fastapi-playground", lifespan=lifespan)

app.include_router(users.router)
app.include_router(items.router, dependencies=[Depends(authorized)])
app.include_router(notifications.router)
app.include_router(queues.router)
app.include_router(exceptions.router)
app.include_router(upload.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(verify_query_token)],
    responses={418: {"description": "I'm a teapot"}},
)
register_exception_handlers(app)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


# https://stackoverflow.com/questions/63206332/how-can-i-list-all-defined-url-paths-in-fastapi
@app.get("/url-list")
def get_all_urls():
    # import inspect

    # for route in app.routes:
    #     print("-" * 20)
    #     for i in inspect.getmembers(route):
    #         print(i)
    url_list = [
        {"path": route.path, "name": route.name, "methods": route.methods}
        for route in app.routes
    ]
    return url_list
