import queue
import time
import concurrent
from contextlib import asynccontextmanager
from fastapi import FastAPI


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


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("startup")
    # pick up existing tasks
    for i in range(5):
        q.put(i)
    executor.submit(run_background_task)

    yield

    print("shutdown")
    q.put(None)
