FROM python:3.9-slim

# Instalează dependințele sistem și Python
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl wget && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir requests flask

WORKDIR /app
COPY . .

EXPOSE 5000
CMD ["python", "main.py"]
