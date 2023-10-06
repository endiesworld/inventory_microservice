dependencies:
	@pip-compile ./inventory_services/requirements.in -o ./inventory_services/requirements.txt
	@pip-compile ./inventory_services/requirements.in ./inventory_services/requirements-dev.in -o ./inventory_services/requirements-dev.txt
	pip-sync ./inventory_services/requirements-dev.txt
	@pip-compile ./payment_services/requirements.in -o ./payment_services/requirements.txt
	@pip-compile ./payment_services/requirements.in ./payment_services/requirements-dev.in -o ./payment_services/requirements-dev.txt
	pip-sync ./payment_services/requirements-dev.txt

lint: black-src isort-src ruff-src

lint-fix: ruff-fix-src

black-src:
	black ./app

isort-src:
	isort ./app

ruff-src:
	ruff ./app

ruff-fix-src:
	ruff ./app --fix

mypy-src:
	mypy ./app

lint-test: black-test isort-test ruff-test

lint-fix-test: ruff-test

black-test:
	black ./app/tests
	black ./app/tests_seeder

isort-test:
	isort ./app/tests
	isort ./app/tests_seeder

ruff-test:
	ruff ./app/tests
	ruff ./app/tests_seeder

ruff-fix-test:
	ruff ./app/tests --fix

mypy-test:
	mypy ./app/tests

stop:
	docker-compose down --remove-orphans

start: stop
	docker-compose up --build

daemon: stop
	docker-compose up --build -d

dev: stop
	STAGE=dev docker-compose -f docker-compose-with-local-db.yml up --build

console:
	docker-compose exec inventory-management-backend python -m asyncio

devtest:
	docker-compose exec inventory-management-backend pytest -s -v app/tests/${TEST_FILE}

test:
	STAGE=dev docker-compose -f docker-compose-test.yml up --build --remove-orphans --exit-code-from inventory-management-backend-test
	$(MAKE) cleantest


