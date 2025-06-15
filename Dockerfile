FROM python:3.9-slim

# Instalează curl pentru depanare
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .
RUN pip install flask

EXPOSE 5000
CMD ["python", "main.py"]
