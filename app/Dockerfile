# 1. Базовый образ с Python
FROM python:3.12

# 2. Устанавливаем рабочую директорию
WORKDIR /app

# 3. Копируем файлы зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Копируем код приложения
COPY . .

# 5. Указываем команду для запуска
CMD ["python", "app.py"]

#FROM python:3.9-slim
#
#WORKDIR /app
#
#COPY app.py /app/
#RUN
#
#ENV FLASK_RUN_HOST=0.0.0.0
#EXPOSE 5000
#
#CMD ["python", "app.py"]