.PHONY: up
up:
	docker compose up --force-recreate --build --watch --remove-orphans
