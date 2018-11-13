FROM python:3.6.6

# FROM python:3.6-slim-jessie
# RUN apt-get update && apt-get install -y --no-install-recommends \
#    wget \
#    gcc

# Dumb init
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 \
    && chmod +x /usr/local/bin/dumb-init

WORKDIR /opt/dask

# Install packages specified in requirements.txt
ADD ./requirements.txt .
RUN pip install --trusted-host pypi.python.org -r requirements.txt