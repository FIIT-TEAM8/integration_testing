FROM python:3.9-alpine

WORKDIR /app

COPY integration_tests.py /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

CMD ["python", "./integration_tests.py"]