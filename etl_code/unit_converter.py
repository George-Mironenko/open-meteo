from datetime import datetime

def fahrenheit_to_celsius(fahrenheit):
    """
    Конвертирует температуру из Фаренгейтов в Цельсии.

    Аргументы:
        fahrenheit (float): Температура в Фаренгейтах

    Возвращает:
        float: Температура в Цельсиях
    """
    return (fahrenheit - 32) / 1.8


def inches_to_millimeters(inches):
    """
    Конвертирует длину из дюймов в миллиметры.

    Аргументы:
        inches (float): Длина в дюймах

    Возвращает:
        float: Длина в миллиметрах
    """
    return inches * 25.4


def knots_to_meters_per_second(knots):
    """
    Конвертирует скорость из узлов в метры в секунду.

    Аргументы:
        knots (float): Скорость в узлах

    Возвращает:
        float: Скорость в метрах в секунду
    """
    return knots * 0.514444

def build_api_url(start_date, end_date) -> str:
    """
    Функция для, создание ссылки с ограниченными датами.
    :param start_date: Дата начала интервала
    :param end_date: Дата конца интервала
    :return: Готовую ссылку с интервалом времени
    """
    with open("API", "r") as file:
        api_url = file.read()

    return f"{api_url}start_date={start_date}&end_date={end_date}"

def validate_date_format(date_str):
    """
    Проверяет, что строка соответствует формату YYYY-MM-DD и является реальной датой.
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Неверный формат даты: {date_str}. Ожидается формат YYYY-MM-DD.")
