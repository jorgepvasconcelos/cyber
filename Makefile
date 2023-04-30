CELERY_BIN_PATH = celery
APP_PATH = task_app.celery_app
CELERY_ARGS = -A $(APP_PATH) worker --loglevel=INFO
FLOWER_ARGS = -A $(APP_PATH) flower --loglevel=INFO

run_api:
	export PYTHONPATH="${PYTHONPATH}:$PWD" && poetry run python ./api/main.py

run_celery:
	$(CELERY_BIN_PATH) $(CELERY_ARGS)

run_flower:
	$(CELERY_BIN_PATH) $(FLOWER_ARGS)

run:
	docker-compose up

requirements: ## Update requirements.txt
	poetry export --without  dev --output requirements.txt --without-hashes
