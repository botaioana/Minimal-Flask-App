FROM python:3.11-alpine

# Instalează dependințe necesare (Alpine folosește `apk` în loc de `apt`)
RUN apk add --no-cache gcc musl-dev && \
    pip install --no-cache-dir requests flask

WORKDIR /app
COPY . .

EXPOSE 5000
CMD ["python", "main.py"]
