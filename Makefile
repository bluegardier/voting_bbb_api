.PHONY: build_voting_api run_voting_api build_consumer run_consumer compose create_topic down reboot

build_voting_api:
	docker build -t voting_api -f ./app/dockerfile ./app

run_voting_api:
	docker run -p 8000:8000 voting_api

build_consumer:
	docker build -t consumer_bbb -f ./consumer/dockerfile ./consumer

run_consumer:
	docker run consumer_bbb

create_topic:
	@echo "📦 Creating Kafka topic 'votes' (if not already exists)..."
	@if docker exec kafka kafka-topics --list --bootstrap-server kafka:9092 | grep -q '^votes$$'; then \
		echo "Topic 'votes' already exists, skipping creation."; \
	else \
		docker exec kafka kafka-topics --create --topic votes --bootstrap-server kafka:9092 --replication-factor 1 --partitions 3; \
	fi

compose:
	docker-compose up --build --force-recreate --scale voting_api=3 -d
	@sleep 10
	$(MAKE) create_topic

down:
	docker-compose down --volumes --remove-orphans

reboot:
	$(MAKE) down
	$(MAKE) compose

