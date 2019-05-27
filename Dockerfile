FROM python:3.7-alpine

WORKDIR /src/app

COPY . .

RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
 && pip3 install -r requirements.txt \
 && apk del .build-deps

EXPOSE 5000

CMD ["python", "webapi.py"]