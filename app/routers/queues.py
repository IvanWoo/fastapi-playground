import queue
import time
import concurrent

from fastapi import APIRouter
from fastapi import status
from fastapi.responses import JSONResponse

router = APIRouter()

q = queue.Queue()
# one task at the same time
# 1 worker to get rid of the lock
executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)


# background task function
def run_background_task():
    while True:
        item = q.get()
        if item is None:
            break
        print(f"processing item {item}")
        # perform some work here
        time.sleep(2)
        print(f"processed item {item}")


@router.post("/queue")
async def add_item(item: str):
    q.put(item)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": f"accepted adding item: {item}"},
    )


@router.on_event("startup")
async def startup_event():
    # pick up existing tasks
    for i in range(5):
        q.put(i)
    executor.submit(run_background_task)


@router.on_event("shutdown")
async def shutdown_event():
    q.put(None)
