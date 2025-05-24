.PHONY: build run execute

build:
	docker build -t voting_api .

run:
	docker run -p 8000:8000 voting_api

compose:
	docker-compose up -d --build --force-recreate

compose_down:
	docker-compose down --volumes --remove-orphans





