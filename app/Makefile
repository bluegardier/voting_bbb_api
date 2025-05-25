.PHONY: build run execute down

build:
	docker build -t voting_api .

run:
	docker run -p 8000:8000 voting_api


compose:
	docker-compose up --build --force-recreate --scale voting_api=3 -d
	@echo "Booting Kafka service..."
	sleep 10
	@echo "Creating "votes" topic in Kafka..."
	docker exec kafka kafka-topics --create --topic votes --bootstrap-server kafka:9092 --replication-factor 1 --partitions 3 || true


down:
	docker-compose down --volumes --remove-orphans





