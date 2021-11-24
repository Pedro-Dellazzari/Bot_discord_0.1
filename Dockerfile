FROM python:3.9
MAINTAINER Erik Hakamada

WORKDIR /usr/src/app

COPY bot.py /usr/src/app
COPY requirements.txt /usr/src/app
COPY token.txt /usr/src/app

RUN ls -lh

RUN python -m venv myenv
CMD ["source", "myenv/bin/activate"]
RUN pip install -r requirements.txt

RUN python bot.py