from task_app.celery_app import app


@app.task(name='send_form_cyber')
def send_form_cyber():
    return 'this is a success task'
