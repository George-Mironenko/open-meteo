# Используем официальный образ Python
FROM python:3.11-slim

# Создаём рабочую директорию внутри контейнера
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код в контейнер
COPY etl_code/ .

# Запуск приложения
CMD ["python", "main.py"]
