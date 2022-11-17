ARG APP_PATH=/opt

FROM python:3.9.15-slim

ARG APP_PATH
WORKDIR $APP_PATH

RUN echo "deb http://deb.debian.org/debian/ unstable main contrib non-free" >> /etc/apt/sources.list.d/debian.list
RUN apt-get update && apt-get upgrade -y
RUN apt-get install libegl-dev libpci-dev -y
# RUN apt-get install -y --no-install-recommends firefox

RUN apt-get install wget -y
RUN apt-get install xz-utils -y

RUN wget https://www.torproject.org/dist/torbrowser/11.5.7/tor-browser-linux64-11.5.7_en-US.tar.xz -O ./tor-browser-linux.tar.xz
RUN tar -xvJf ./tor-browser-linux.tar.xz
RUN apt-get install tor -y

COPY ./src $APP_PATH/src
COPY ./scraping_url.py $APP_PATH/scraping_url.py
COPY ./requirements.txt $APP_PATH/requirements.txt

RUN pip install -r $APP_PATH/requirements.txt --no-cache-dir

RUN service tor restart

CMD ["python", "scraping_url.py"]
