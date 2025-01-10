from app.workers.celery import app
from celery import Task


class NotificationTask(Task):
    autoretry_for = (Exception,)
    retry_kwargs = {"max_retries": 5, "countdown": 60}
    retry_backoff = True


@app.task(base=NotificationTask)
def send_notification_task(email: str) -> int:
    print(f"notification sent to {email}")
    return 1
