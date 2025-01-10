from celery import Celery

app = Celery("fastapi-playground.workers")
app.config_from_object("app.workers.celery_config")

if __name__ == "__main__":
    app.start()
