FROM python:3.8-slim-buster

RUN apt-get update

RUN pip install awscli

RUN pip install --upgrade pip

WORKDIR /app

COPY . /aap

RUN python3 -m pip install -r requirements.txt

CMD ["python3", "app.py"]
