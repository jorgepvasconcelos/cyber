CELERY_BIN_PATH = celery
APP_PATH = celery_app
CELERY_ARGS = -A $(APP_PATH) worker --loglevel=INFO
FLOWER_ARGS = -A $(APP_PATH) flower --loglevel=INFO

run_celery:
	$(CELERY_BIN_PATH) $(CELERY_ARGS)

run_flower:
	$(CELERY_BIN_PATH) $(FLOWER_ARGS)

container:
	docker-compose up

#run: container run_celery
