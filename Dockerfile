FROM python:3.9-slim

LABEL maintainer="kirisame@mco.moe"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV APP_PRODUCTION=True
ENV APP_DB_PATH=/data

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-warn-script-location --no-cache-dir --user -r requirements.txt

COPY ./src .
COPY ./docker/entrypoint.sh /usr/local/bin

RUN mkdir -p ${APP_DB_PATH} && chmod +x /usr/local/bin/entrypoint.sh

VOLUME [ "/data" ]

ENTRYPOINT ["entrypoint.sh"]
