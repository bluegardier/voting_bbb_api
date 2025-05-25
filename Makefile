.PHONY: build run execute down

build:
	docker build -t voting_api .

run:
	docker run -p 8000:8000 voting_api

compose:
	docker-compose up --build --force-recreate --scale voting_api=3 -d

down:
	docker-compose down --volumes --remove-orphans





