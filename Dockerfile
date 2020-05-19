FROM python:3.8-slim-buster

RUN pip install pipenv

COPY Pipfile /Pipfile
COPY Pipfile.lock /Pipfile.lock

RUN pipenv install --system --deploy

COPY main.py /main.py

CMD ["python", "main.py"]
