import os
import time

from celery import Celery
from celery import group
from celery.result import GroupResult

from sdk import get_weather

celery_app = Celery(__name__)

celery_app.conf.broker_url = os.environ.get(
    "CELERY_BROKER_URL", "amqp://user:mypass@rabbitmq:5672//"
)
celery_app.conf.result_backend = os.environ.get(
    "CELERY_RESULT_BACKEND",
    "db+postgresql://user:mypass@postgres:5432/postgres",
)

celery_app.conf.update(result_extended=True)


@celery_app.task(name="create_task", rate_limit="60/m")
def create_task(city_id):
    return get_weather(city_id)


def create_multi_tasks(request_id, cities) -> str:
    job = group(create_task.s(city_id) for city_id in cities)
    result = job.apply_async()
    result.save()
    return result.id


def get_tasks_completion(request_id):
    results = GroupResult.restore(request_id, app=celery_app)
    successful = [r.successful() for r in results]
    return (sum(successful) / len(successful)) * 100.0


def get_results(request_id):
    results = GroupResult.restore(request_id, app=celery_app)
    successful = [r.result for r in results if r.successful()]
    return successful
