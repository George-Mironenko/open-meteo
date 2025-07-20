# Используем официальный образ Python
FROM python:3.11-slim

# Определяем аргументы сборки
ARG START_DATE
ARG END_DATE

# Проверяем, что они заданы
RUN if [ -z "${START_DATE}" ]; then echo "Ошибка: START_DATE не указан"; exit 1; fi
RUN if [ -z "${END_DATE}" ]; then echo "Ошибка: END_DATE не указан"; exit 1; fi

# Сохраняем их как переменные окружения (если нужно)
ENV START_DATE=${START_DATE}
ENV END_DATE=${END_DATE}

# Создаём рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код
COPY . .

# Запуск приложения
CMD ["python", "main.py"]