from celery import Celery

from task_app import celeryconfig
from settings import CELERY_APP_NAME


def send_task(task_name: str) -> str:
    app = Celery(CELERY_APP_NAME, config_source=celeryconfig)
    result = app.send_task(name=task_name, queue=CELERY_APP_NAME)
    return result


if __name__ == '__main__':
    send_task(task_name='send_form_cyber')
