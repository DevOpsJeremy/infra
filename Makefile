.PHONY: up test
up:
	docker compose up --remove-orphans --force-recreate --build

test:
	docker compose run --remove-orphans --rm python ruff check
	docker compose run --remove-orphans --rm python ruff format --check
# 	docker compose run --remove-orphans --rm python pytest
	docker compose run --remove-orphans --rm ansible-lint ansible-lint
