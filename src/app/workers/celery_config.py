REDIS_URL = "redis://:password@localhost:6379/0"

broker_url = REDIS_URL
result_backend = REDIS_URL

include = ["app.workers.tasks"]

task_acks_later = True
task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]
result_expires = 3600

timezone = "UTC"
enable_utc = True

broker_connection_retry_on_startup = True

task_routes = {
    "*": {"queue": "default"},
}
