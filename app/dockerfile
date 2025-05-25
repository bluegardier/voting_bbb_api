FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    nano \
    curl \
    iputils-ping \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /project

COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8000

CMD ["python3", "main.py"]
