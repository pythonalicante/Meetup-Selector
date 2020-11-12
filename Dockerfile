FROM python:3.8

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt \
    && mkdir /usr/src/app/tmp \
    && chmod +x docker-entrypoint.sh

