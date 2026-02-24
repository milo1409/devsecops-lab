FROM python:3.12-slim

# Variables para evitar archivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y gcc

# Copiar requirements primero (optimiza cache)
COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la app
COPY app/ .

EXPOSE 8080

CMD ["gunicorn", "demo.wsgi:application", "--bind", "0.0.0.0:8080"]
