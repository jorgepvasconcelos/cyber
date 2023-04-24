from celery import Celery

from task_app import celeryconfig
from settings import REDIS_URL, CELERY_APP_NAME

app = Celery(
    main=CELERY_APP_NAME,
    backend=REDIS_URL,
    broker=REDIS_URL,
    include=['task_app.tasks'],
    config_source=celeryconfig
)

if __name__ == '__main__':
    app.start()
