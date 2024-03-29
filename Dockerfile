FROM python:3.7-slim as app

RUN apt-get update -y && apt-get install -y \
            build-essential \
            ffmpeg \
            gettext \
            libavcodec-extra \
            gcc \
            libpcre3 \
            libpcre3-dev \
        && apt-get clean

RUN adduser --disabled-password poetica
USER poetica
WORKDIR /home/poetica
ENV PATH=$PATH:/home/poetica/.local/bin

COPY --chown=poetica:poetica requirements.txt .

RUN pip install --user --no-cache-dir -r requirements.txt

COPY --chown=poetica:poetica . .

FROM app AS test

RUN pip install --user --no-cache-dir -r dev_requirements.txt
