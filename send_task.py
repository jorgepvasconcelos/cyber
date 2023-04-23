from celery import Celery

import celeryconfig
from settings import CELERY_APP_NAME

app = Celery(CELERY_APP_NAME, config_source=celeryconfig)
result = app.send_task(name='send_form_cyber',queue=CELERY_APP_NAME)
print(result)