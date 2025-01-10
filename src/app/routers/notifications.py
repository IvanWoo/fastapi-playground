from fastapi import BackgroundTasks
from fastapi import APIRouter
from app.workers.tasks import send_notification_task

router = APIRouter()


async def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)


@router.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    send_notification_task.delay(email)
    return {"message": "Notification sent in the background"}
