# Stage 1: Dpendencies
FROM docker.arvancloud.ir/python:3.11.10-slim as requirements_builder
LABEL authors="Erfan Arefmehr"

ENV PIP_DEFAULT_TIMEOUT=1000 \
    # Allow statements and log messages to immediately appear
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    # disable a pip version check to reduce run-time & log-spam
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    # cache is useless in docker image, so disable to reduce image size
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.7.1

WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN pip install "poetry==$POETRY_VERSION" \
    && poetry install --no-root --no-ansi --no-interaction \
    && poetry export -f requirements.txt -o requirements.txt

# Stage 2: Build
FROM docker.arvancloud.ir/python:3.11.10-slim
RUN apt update

WORKDIR /app/
COPY --from=requirements_builder /app/requirements.txt .

RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8000:8000

CMD ["fastapi", "run"]
