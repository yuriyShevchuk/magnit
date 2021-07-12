FROM python:3.9.6

ENV DockerHOME=/home/app/magnit
RUN mkdir -p $DockerHOME
WORKDIR $DockerHOME
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY . $DockerHOME
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin libgdal-dev
RUN pip install --upgrade pip &&\
    pip install -r requirements.txt
