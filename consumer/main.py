import json
from config import Settings
from src.factories.database_factory import DatabaseFactory
from src.factories.queue_factory import QueueFactory
from src.logger import default_logger


def main():
    settings = Settings()
    db_strategy = DatabaseFactory.create(settings)
    queue_strategy = QueueFactory.create(settings)

    buffer = []

    try:
        for vote in queue_strategy.consume():
            default_logger.info(f"Received vote type: {type(vote)}, value: {vote}")
            if isinstance(vote, str):
                vote = json.loads(vote)
            buffer.append(vote)
            default_logger.debug(f"Message received and added to buffer: {vote}")

            if len(buffer) >= settings.buffer_size:
                default_logger.info(f"Inserting {len(buffer)} votes into the database.")
                for v in buffer:
                    try:
                        db_strategy.insert_vote(v)
                        default_logger.debug(f"Vote successfully inserted: {v}")
                    except Exception as e:
                        default_logger.error(
                            f"Error inserting vote {v}: {e}", exc_info=True
                        )
                buffer.clear()
    except Exception as e:
        default_logger.critical(
            "Fatal error while consuming messages from the queue", exc_info=True
        )


if __name__ == "__main__":
    main()
