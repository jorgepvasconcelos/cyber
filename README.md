# Form Sender

## Built With:
- [Python](https://www.python.org/) - Programming language
- [FastAPI](https://fastapi.tiangolo.com/) - Web Framework
- [Redis](https://redis.io/) - Message Broker
- [Celery](https://docs.celeryq.dev/en/stable/index.html) - Task queue
- [Flower](https://flower.readthedocs.io/en/latest/) - Celery task queue monitor
- [Selenium](https://www.selenium.dev/) - Automation tool


## Project propose
This project uses automation to fill and send https://cyberintelligencehouse.com/ "Partner with us" Form 

## Requirements to run
- docker
- curl
- make
- 2captcha API TOKEN

## How to run
1 - create an env.env file based on env.env-exemple passing your values   
2 - Run the command to start docker containers:
```
make run
```
3 - Run the command to send a task to the queue:
```
curl --location 'localhost:8080/task_deliver' \
--header 'Content-Type: application/json' \
--data '{
    "task_name": "send_form_cyber"
}'
```
4 - Observe the automation in http://localhost:4444/ui   

## URL Services
Selenium - http://localhost:4444/ui   
Fastapi - http://localhost:8080  
Flower - http://localhost:5555