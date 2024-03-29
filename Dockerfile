FROM python:slim-buster

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python3", "app/app.py"]