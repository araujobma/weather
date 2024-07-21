import os
import time

from celery import Celery

celery_app = Celery(__name__)

celery_app.conf.broker_url = os.environ.get(
    "CELERY_BROKER_URL", "amqp://user:mypass@rabbitmq:5672//"
)
# celery_app.conf.result_backend = os.environ.get(
#     "CELERY_RESULT_BACKEND",
#     "db+postgresql://myuser:mypassword@localhost:5432/mydatabase",
# )


@celery_app.task(name="create_task")
def create_task(task_type):
    print(task_type)
    time.sleep(int(task_type) * 10)
    return True
