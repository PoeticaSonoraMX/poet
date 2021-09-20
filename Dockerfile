FROM python:3.7-slim as app

RUN apt-get update -y && apt-get install -y \
            ffmpeg \
            gettext \
            libavcodec-extra \
            gcc \
            libpcre3 \
            libpcre3-dev \
        && apt-get clean

RUN mkdir /home/poet && cd /home/poet
RUN adduser --disabled-password poetica
USER poetica
WORKDIR /home/poet

COPY requirements.txt .

RUN pip install --user --no-cache-dir -r requirements.txt

COPY . .

FROM app AS test

RUN pip install --user --no-cache-dir -r dev_requirements.txt
