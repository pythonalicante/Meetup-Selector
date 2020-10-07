FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir ./tmp
VOLUME /usr/src/app/tmp

RUN chmod +x docker-entrypoint.sh

EXPOSE 8000

CMD ["./docker-entrypoint.sh"]

