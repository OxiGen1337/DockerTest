FROM python:3.12

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем файлы приложения
COPY . .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Открываем порт 5000
EXPOSE 5000

# Команда запуска приложения
CMD ["python", "app.py"]
