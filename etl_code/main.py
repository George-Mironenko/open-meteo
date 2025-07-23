import os
import argparse

from etl_process import extract_transform_load
from unit_converter import validate_date_format



def main():
    try:
        # Парсим аргументы из командной строки или из переменных окружения
        parser = argparse.ArgumentParser()
        parser.add_argument("--start_date", type=str, help="Start date (YYYY-MM-DD)")
        parser.add_argument("--end_date", type=str, help="End date (YYYY-MM-DD)")
        args = parser.parse_args()

        # Если даты не переданы через CLI, попробовать из переменных окружения
        start_date = args.start_date or os.getenv("START_DATE")
        end_date = args.end_date or os.getenv("END_DATE")

        # Если даты не заданы — ошибка
        if not start_date or not end_date:
            raise ValueError("Не указаны start_date и end_date")

        # Проверка формата дат
        validate_date_format(start_date)
        validate_date_format(end_date)

    except ValueError as ve:
        print(f"Ошибка валидации дат: {ve}")
        exit(1)
    except Exception as error:
        print("Ошибка ", error)
        exit(1)
    else:
        # Запуск основного ETL-процесса
        extract_transform_load(start_date, end_date)

if __name__ == "__main__":
    main()