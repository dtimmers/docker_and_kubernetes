FROM python:3.7-slim-buster

WORKDIR /usr/app

# install Flask
COPY ./requirements.txt ./
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# copy over the flask api definition
COPY ./ ./

# start the api
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--log-level", "debug", "app_client:app"]

