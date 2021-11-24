FROM python:3.9
MAINTAINER Erik Hakamada

WORKDIR /temp/ffmpeg
COPY ffmpeg.orig.tar.xz /temp/ffmpeg
RUN tar -xf ffmpeg.orig.tar.xz > ffmpeg
CMD ./ffmpeg-4.4.1/configure && make
CMD make install

WORKDIR /usr/src/app
COPY bot.py /usr/src/app
COPY requirements.txt /usr/src/app
COPY token.txt /usr/src/app

RUN python -m venv env
CMD ["source", "env/bin/activate"]
CMD ["/usr/local/bin/python", "-m", "pip", "install" ,"--upgrade", "pip"]
RUN pip install -r requirements.txt

RUN python bot.py

#FROM python:3.9
#WORKDIR /usr/app
#COPY . /usr/app
#ENTRYPOINT python