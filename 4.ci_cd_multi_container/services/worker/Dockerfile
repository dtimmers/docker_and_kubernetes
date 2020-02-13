# need pg_info binary
FROM python:3.7-slim-buster

WORKDIR /usr/app

# install python dependencies
COPY ./requirements.txt ./
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# copy over the listener definition
COPY ./ ./

CMD ["python", "-u", "worker.py"]