FROM python:3.12.1-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predict.py", "predict-test.py", "model_C=1.bin", "./"]

EXPOSE 5454

ENTRYPOINT ["waitress-serve", "--listen=0.0.0.0:5454", "predict:app"]