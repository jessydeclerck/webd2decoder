FROM python:3.7-alpine

WORKDIR /src/app
ENV PYTHONPATH=/src/app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD [ "gunicorn", "d2decoder.wsgi:application", "--bind", "0.0.0.0:8000" ]