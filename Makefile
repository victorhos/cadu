MANAGE_PY=django/manage.py
DJANGO_PATH=django/cadu/
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

create-app:
	@python $(MANAGE_PY) startapp $(name) --settings=$(DEV_SETTINGS)

load-customers:
	@python $(MANAGE_PY) load_customers $(url) --settings=$(DEV_SETTINGS)

requirements-dev:
	@pip install -U -r django/requirements/development.txt

clean: ## Clean local environment
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -rf htmlcov/
	@rm -f coverage.xml
	@rm -f *.log

test: clean
	@py.test -x django/cadu

test-matching:
	@py.test -rxs -k $(Q) --pdb django/cadu

coverage: clean
	@py.test -x --cov django/cadu/ --cov-config=.coveragerc --cov-report=term --cov-report=html --cov-report=xml

fix-python-import:
	@isort -rc .
