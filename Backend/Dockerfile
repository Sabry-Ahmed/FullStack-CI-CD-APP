FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5001

ENV NAME World

CMD ["python3", "app.py"]
