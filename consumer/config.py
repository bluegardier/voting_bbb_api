from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database config
    db_strategy: str = Field("postgres", env="DB_STRATEGY")
    db_host: str = Field("localhost", env="DB_HOST")
    db_port: int = Field(5432, env="DB_PORT")
    db_user: str = Field("voting_user", env="DB_USER")
    db_password: str = Field("voting_password", env="DB_PASSWORD")
    db_name: str = Field("voting_db", env="DB_NAME")

    # Kafka config
    queue_strategy: str = Field("kafka", env="QUEUE_STRATEGY")
    kafka_bootstrap_servers: str = Field(
        "kafka:9092", env="KAFKA_BOOTSTRAP_SERVERS"
    )
    kafka_topic: str = Field("votes", env="KAFKA_TOPIC")

    # Flush Parameters
    buffer_size: int = Field(1000, env="KAFKA_BUFFER_SIZE")
    buffer_timer: int = Field(180, env="KAFKA_BUFFER_TIMER")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
