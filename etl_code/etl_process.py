# Библиотека для выполнения HTTP-запросов
import requests
# Библиотека для обработки данных
import pandas as pd

# Импортируем функции из модуля unit_converter.py
from unit_converter import (fahrenheit_to_celsius,
                            inches_to_millimeters, knots_to_meters_per_second)
from data_base import PostgresConnection


# Читаем файл с API
with open("API", "r") as file:
    API_URL = file.read()

# Делаем HTTP-запрос
response = requests.get(API_URL)
# Преобразовываем данные в формат JSON
data = response.json()


def insert_to_db(daily_df):
    db = PostgresConnection(
        database="database",
        user="users",
        password="password",
        port=5432,
        host="db"
    )
    try:
        query = """
            INSERT INTO daily_weather (
                date,
                avg_temperature_2m_24h,
                avg_relative_humidity_2m_24h,
                avg_dew_point_2m_24h,
                avg_apparent_temperature_24h,
                avg_temperature_80m_24h,
                avg_temperature_120m_24h,
                avg_wind_speed_10m_24h,
                avg_wind_speed_80m_24h,
                avg_visibility_24h,
                total_rain_24h,
                total_showers_24h,
                total_snowfall_24h
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (date) DO NOTHING;
        """

        for _, row in daily_df.iterrows():
            db.execute(query, tuple(row))

    except Exception as error:
        print("Ошибка ", error)
    else:
        db.commit()
    finally:
        db.close()


def extract_transform_load():
    # Преобразуем все необходимые поля
    hourly = data["hourly"]
    df = pd.DataFrame({
        "datetime": pd.to_datetime(hourly["time"], unit="s"),
        "temperature_2m": hourly["temperature_2m"],
        "relative_humidity_2m": hourly["relative_humidity_2m"],
        "dew_point_2m": hourly["dew_point_2m"],
        "apparent_temperature": hourly["apparent_temperature"],
        "temperature_80m": hourly["temperature_80m"],
        "temperature_120m": hourly["temperature_120m"],
        "wind_speed_10m": hourly["wind_speed_10m"],
        "wind_speed_80m": hourly["wind_speed_80m"],
        "visibility": hourly["visibility"],
        "rain": hourly["rain"],
        "showers": hourly["showers"],
        "snowfall": hourly["snowfall"]
    })

    # Добавляем столбец с датой
    df["date"] = df["datetime"].dt.date

    # Средние значения по суткам
    daily = df.groupby("date").agg({
        "temperature_2m": lambda x: fahrenheit_to_celsius(x).mean(),
        "relative_humidity_2m": "mean",
        "dew_point_2m": lambda x: fahrenheit_to_celsius(x).mean(),
        "apparent_temperature": lambda x: fahrenheit_to_celsius(x).mean(),
        "temperature_80m": lambda x: fahrenheit_to_celsius(x).mean(),
        "temperature_120m": lambda x: fahrenheit_to_celsius(x).mean(),
        "wind_speed_10m": lambda x: knots_to_meters_per_second(x).mean(),
        "wind_speed_80m": lambda x: knots_to_meters_per_second(x).mean(),
        "visibility": lambda x: x.mean() * 0.3048,
        "rain": lambda x: inches_to_millimeters(x).sum(),
        "showers": lambda x: inches_to_millimeters(x).sum(),
        "snowfall": lambda x: inches_to_millimeters(x).sum(),
    }).reset_index()

    # Переименовываем столбцы
    daily.columns = [
        "date",
        "avg_temperature_2m_24h",
        "avg_relative_humidity_2m_24h",
        "avg_dew_point_2m_24h",
        "avg_apparent_temperature_24h",
        "avg_temperature_80m_24h",
        "avg_temperature_120m_24h",
        "avg_wind_speed_10m_24h",
        "avg_wind_speed_80m_24h",
        "avg_visibility_24h",
        "total_rain_24h",
        "total_showers_24h",
        "total_snowfall_24h"
    ]

    # Сохраняем данные в формате csv
    daily.to_csv("weather_data.csv", index=False)

    # Вставка в БД
    insert_to_db(daily)
