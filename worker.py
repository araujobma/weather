import os
import time

from celery import Celery
from celery import group
from celery.result import GroupResult

celery_app = Celery(__name__)

celery_app.conf.broker_url = os.environ.get(
    "CELERY_BROKER_URL", "amqp://user:mypass@rabbitmq:5672//"
)
celery_app.conf.result_backend = os.environ.get(
    "CELERY_RESULT_BACKEND",
    "db+postgresql://user:mypass@postgres:5432/db",
)

celery_app.conf.update(result_extended=True)


@celery_app.task(name="create_task")
def create_task(city_id):
    print(city_id)
    time.sleep(10)
    return True


def create_multi_tasks(request_id, cities):
    job = group(create_task.s(city_id) for city_id in cities[0:30])
    result = job.apply_async()
    result.save()
    print("RESULT GROUP ID:", result.id)


def get_tasks_completion(request_id):
    results = GroupResult.restore(request_id, app=celery_app)
    successful = [r.successful() for r in results]
    return (sum(successful) / len(successful)) * 100.0


def get_results(request_id):
    results = GroupResult.restore(request_id, app=celery_app)
    successful = [{"result": r.result} for r in results if r.successful()]
    return successful
