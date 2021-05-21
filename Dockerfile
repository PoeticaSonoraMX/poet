FROM python:3.7-slim as app

RUN mkdir /home/poet && cd /home/poet

WORKDIR /home/poet

RUN apt-get update -y && apt-get install -y \
            ffmpeg \
            gettext \
            libavcodec-extra \
            gcc \
        && apt-get clean

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

FROM app AS test

RUN pip install --no-cache-dir -r dev_requirements.txt
