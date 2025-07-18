import psycopg2
from typing import Optional, Tuple
import logging

class PostgresConnection:
    """Класс для подключения к PostgreSQL."""

    def __init__(
        self,
        database: str,
        password: str,
        host: str = "localhost",
        user: str = "postgres",
        port: int = 5432
    ) -> None:
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.connection = None
        self.cursor = None
        self._connect()

    def _connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            logging.info("Подключение к PostgreSQL установлено.")
        except psycopg2.Error as e:
            logging.critical(f"Ошибка подключения: {e}")
            raise

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
            logging.info("✅ Соединение с PostgreSQL закрыто.")
        except Exception as e:
            logging.error(f"Ошибка при закрытии: {e}")

    def commit(self):
        try:
            self.connection.commit()
        except Exception as e:
            logging.error(f"Ошибка при commit: {e}")

    def execute(self, query: str, params: Optional[Tuple] = None) -> bool:
        try:
            self.cursor.execute(query, params or ())
            return True
        except psycopg2.Error as e:
            logging.error(f"Ошибка при выполнении запроса: {e}")
            return False
