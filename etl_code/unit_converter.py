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