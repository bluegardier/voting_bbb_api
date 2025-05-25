import psycopg2
from src.strategies.database.base import DatabaseStrategy


class PostgresDatabase(DatabaseStrategy):
    def __init__(self, settings):
        self.conn = psycopg2.connect(
            host=settings.db_host,
            port=settings.db_port,
            user=settings.db_user,
            password=settings.db_password,
            dbname=settings.db_name,
        )
        self.conn.autocommit = True

    def insert_vote(self, vote_data):
        with self.conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO voting_bbb_table 
                (request_id, timestamp, arthur_aguiar, davi_brito, yagami_light)
                VALUES (%s, %s, %s, %s, %s)
            """,
                (
                    vote_data["request_id"],
                    vote_data["timestamp"],
                    vote_data["arthur_aguiar"],
                    vote_data["davi_brito"],
                    vote_data["yagami_light"],
                ),
            )
