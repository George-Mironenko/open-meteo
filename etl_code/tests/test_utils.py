import pytest
# Импортируем функцию для проверки даты
from unit_converter import validate_date_format


# Проверка валидации даты
def test_validate_date_format_valid():
    validate_date_format("2025-07-01")

def test_validate_date_format_invalid():
    with pytest.raises(ValueError):
        validate_date_format("07-01-2025")