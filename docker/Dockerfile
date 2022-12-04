ARG APP_PATH=/opt

FROM python:3.9.15-slim
ARG APP_PATH
WORKDIR $APP_PATH

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libegl-dev libpci-dev libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1

COPY ./source $APP_PATH/source
COPY ./requirements.txt $APP_PATH/requirements.txt
COPY ./.env $APP_PATH/.env

RUN pip install --upgrade pip
RUN pip install -r $APP_PATH/requirements.txt --no-cache-dir
