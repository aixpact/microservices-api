FROM python:3.7-slim

RUN apt-get update && apt-get install -qq -y \
  build-essential libpq-dev libffi-dev sudo --no-install-recommends

ENV INSTALL_PATH /project_path
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
RUN pip install --editable .

CMD gunicorn -w 1 -b 0.0.0.0:7000 --reload --access-logfile - "project.app:create_app()"
