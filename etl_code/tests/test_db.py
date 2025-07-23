import pytest
from unittest.mock import patch, MagicMock

# Импорт тестируемого класса
from data_base import PostgresConnecti


# Тест успешного подключения к базе данных
@patch("psycopg2.connect")
def test_connection_success(mock_connect):
    # Создаем mock-объект для соединения с БД
    mock_conn = MagicMock()
    # Задаем возвращаемое значение для мока connect
    mock_connect.return_value = mock_conn

    db = PostgresConnection(
        database="test_db",
        user="test_user",
        password="test_pass",
        host="localhost",
        port=5432
    )

    # Проверяем, что соединение и курсор были успешно созданы
    assert db.connection is not None
    assert db.cursor is not None
    db.close()

# Тест неудачного подключения к базе данных
@patch("psycopg2.connect", side_effect=Exception("Connection failed"))
def test_connection_failure(mock_connect):
    with pytest.raises(Exception):
        PostgresConnection(
            database="fail_db",
            user="user",
            password="pass"
        )
