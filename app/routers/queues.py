from fastapi import APIRouter
from fastapi import status
from fastapi.responses import JSONResponse
from app.config.lifespan import q

router = APIRouter()


@router.post("/queue")
async def add_item(item: str):
    q.put(item)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": f"accepted adding item: {item}"},
    )
