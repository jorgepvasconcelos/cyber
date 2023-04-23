from celery_app import app
from celery import Task


@app.task(name='send_form_cyber')
def send_form_cyber():
    return 'this is a success task'
