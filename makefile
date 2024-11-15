include .env

DOCKER_COMPOSE = $(shell if docker compose version > /dev/null 2>&1; then echo "docker compose"; else echo "docker-compose"; fi)

run:
	$(DOCKER_COMPOSE) up -d

test:
	docker exec -it docker_cinema_api go test ./... -v

build:
	$(DOCKER_COMPOSE) up --build -d

down:
	$(DOCKER_COMPOSE) down -v

logs:
	docker logs --follow docker_cinema_api

kill-all:
	docker kill $$(docker ps -aq)

rm-all:
	docker rm $$(docker ps -aq)

clean-all:
	docker system prune -a --volumes