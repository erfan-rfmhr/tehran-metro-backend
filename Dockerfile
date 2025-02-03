FROM docker.arvancloud.ir/python:3.11.10-slim
LABEL authors="Erfan Arefmehr"

ENV PIP_DEFAULT_TIMEOUT=1000 \
    # Allow statements and log messages to immediately appear
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    # disable a pip version check to reduce run-time & log-spam
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    # cache is useless in docker image, so disable to reduce image size
    PIP_NO_CACHE_DIR=1

WORKDIR /app
COPY requirements.txt ./

RUN apt update

RUN pip install -r requirements.txt

WORKDIR /app/

COPY . /app/

RUN chmod +x infra/run.sh;

EXPOSE 8000:8000

CMD ["fastapi", "run"]
