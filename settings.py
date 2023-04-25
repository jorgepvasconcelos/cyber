import os

CAPTCHA_API_KEY = os.getenv('CAPTCHA_API_KEY')
REDIS_URL = os.getenv("REDIS_URL")
CELERY_APP_NAME = "celery_cyber"
HOST_SELENIUM_GRID = os.getenv("HOST_SELENIUM_GRID")

