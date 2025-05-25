from src.strategies.database.postgres import PostgresDatabase
from config import Settings


class DatabaseFactory:
    @staticmethod
    def create(settings: Settings):
        strategy = settings.db_strategy.lower()
        if strategy == "postgres":
            return PostgresDatabase(settings)
        else:
            raise ValueError(f"Unsupported DB strategy: {strategy}")
