FROM python:3.13-slim-bookworm

# Instalează doar dependințele necesare (fără curl/wget dacă nu sunt esențiale)
RUN apt-get update && \
    apt-get upgrade -y && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir requests flask

WORKDIR /app
COPY . .

EXPOSE 5000
CMD ["python", "main.py"]
