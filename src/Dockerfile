FROM python:alpine3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /NeoApp;
WORKDIR /NeoApp

ADD requirements.pip /NeoApp
RUN pip install -r /NeoApp/requirements.pip

# Install bash
RUN apk add --no-cache bash gawk sed grep bc coreutils
