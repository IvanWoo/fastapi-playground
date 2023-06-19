from queue import Queue
import time
import concurrent
from contextlib import asynccontextmanager
from fastapi import FastAPI
from typing import Callable, TypeVar

T = TypeVar("T")

q: Queue[int | None] = Queue()
# one task at the same time
# 1 worker to get rid of the lock
executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)


def dummy_background_task(item: int):
    time.sleep(0.2)
    if item % 2 == 0:
        raise Exception("dummy error")


# background task function
def run_background_task(queue: Queue[T], func: Callable[[T], None]) -> None:
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"processing item {item}")
        # perform some work here
        try:
            func(item)
        except Exception as e:
            msg = f"failed to run background for {item=}: {e}"
            print(msg)
        print(f"processed item {item}")


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("startup")
    # pick up existing tasks
    for i in range(5):
        q.put(i)
    executor.submit(run_background_task, q, dummy_background_task)

    yield

    print("shutdown")
    q.put(None)
