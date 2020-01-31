FROM python:3.7-slim-buster

WORKDIR /usr/app

# install Flask
COPY requirements.txt ./
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# copy over the flask server definition
COPY ./ ./

# make sure that port 80 is accessible
EXPOSE 80

# start the server
CMD ["gunicorn", "--bind", "0.0.0.0:80", "index:app"]

