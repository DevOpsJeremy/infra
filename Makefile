.PHONY: up test fix
up: secrets.env
	docker compose up --remove-orphans --force-recreate --build

secrets.env:
	touch secrets.env

test:
	docker compose run --remove-orphans --rm python ruff check
	docker compose run --remove-orphans --rm python ruff format --check
# 	docker compose run --remove-orphans --rm python pytest
	docker compose run --remove-orphans --rm ansible-lint ansible-lint

fix:
	docker compose run --remove-orphans --rm python ruff check --fix
	docker compose run --remove-orphans --rm python ruff format
	docker compose run --remove-orphans --rm ansible-lint ansible-lint --fix
