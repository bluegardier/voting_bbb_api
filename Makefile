.PHONY: build run execute

build:
	docker build -t voting_api .

run:
	docker run -p 8000:8000 voting_api

execute:
	docker build --no-cache -t voting_api . && docker run -p 8000:8000 voting_api
