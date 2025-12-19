.PHONY: up test test-ansible test-python fix
up: secrets.env
	docker compose up --remove-orphans --force-recreate --build

secrets.env:
	touch secrets.env

test: test-python test-ansible

test-ansible:
	docker compose run --remove-orphans --rm ansible-lint ansible-lint

test-python:
	docker compose run --remove-orphans --rm python ruff check
	docker compose run --remove-orphans --rm python ruff format --check
# 	docker compose run --remove-orphans --rm python pytest

fix: fix-python fix-ansible

fix-python:
	docker compose run --remove-orphans --rm python ruff check --fix
	docker compose run --remove-orphans --rm python ruff format

fix-ansible:
	docker compose run --remove-orphans --rm ansible-lint ansible-lint --fix
