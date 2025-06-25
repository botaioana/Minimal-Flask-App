FROM python:3.11-slim-bookworm

# Instalează doar dependințele necesare
RUN apt-get update && \
    apt-get upgrade -y && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir requests flask

WORKDIR /app
COPY . .

EXPOSE 5000
CMD ["python", "main.py"]
