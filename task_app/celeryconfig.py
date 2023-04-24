from kombu import Exchange, Queue

from settings import CELERY_APP_NAME,REDIS_URL

broker_url = REDIS_URL

task_queues = (
    Queue(name=CELERY_APP_NAME, exchange=Exchange(CELERY_APP_NAME, type='direct')),
)
