FROM python:3.7-slim-buster

WORKDIR /usr/app

# install Flask
COPY ./requirements.txt ./
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# copy over the flask server definition
COPY ./index.py ./

CMD ["flask", "run", "--host=0.0.0.0"]