FROM python:3.11-slim-bookworm

# Instalează și actualizează toate pachetele sistem
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends curl wget && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir requests flask

WORKDIR /app
COPY . .

EXPOSE 5000
CMD ["python", "main.py"]
