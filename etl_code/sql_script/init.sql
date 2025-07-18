CREATE TABLE IF NOT EXISTS daily_weather (
    date DATE PRIMARY KEY,
    avg_temperature_2m_24h REAL,
    avg_relative_humidity_2m_24h REAL,
    avg_dew_point_2m_24h REAL,
    avg_apparent_temperature_24h REAL,
    avg_temperature_80m_24h REAL,
    avg_temperature_120m_24h REAL,
    avg_wind_speed_10m_24h REAL,
    avg_wind_speed_80m_24h REAL,
    avg_visibility_24h REAL,
    total_rain_24h REAL,
    total_showers_24h REAL,
    total_snowfall_24h REAL
);
