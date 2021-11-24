FROM python:3.9
MAINTAINER Erik Hakamada

WORKDIR /temp/ffmpeg
RUN wget http://johnvansickle.com/ffmpeg/releases/ffmpeg-release-64bit-static.tar.xz
RUN tar -xf ffmpeg-release-64bit-static.tar.xz
RUN mv ffmpeg-*-64bit-static/ffmpeg /usr/local/bin/
RUN mv ffmpeg-*-64bit-static/ffprobe /usr/local/bin/

WORKDIR /usr/src/app
COPY bot.py /usr/src/app
COPY requirements.txt /usr/src/app
COPY token.txt /usr/src/app

RUN python -m venv env
CMD ["source", "env/bin/activate"]
RUN pip install -r requirements.txt

RUN python bot.py