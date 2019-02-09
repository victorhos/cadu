MANAGE_PY=django/manage.py
DEV_SETTINGS=cadu.settings.development
TEST_SETTINGS=cadu.settings.test
PROD_SETTINGS=cadu.settings.production

shell:
	@python $(MANAGE_PY) shell --settings=$(DEV_SETTINGS)

run:
	@python $(MANAGE_PY) runserver --settings=$(DEV_SETTINGS)

migrate:
	@python $(MANAGE_PY) migrate --settings=$(DEV_SETTINGS)

migrations:
	@python $(MANAGE_PY) makemigrations --settings=$(DEV_SETTINGS)

requirements-dev:
	@pip install -U -r django/requirements/development.txt
