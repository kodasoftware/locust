FROM python:3.8
LABEL Maintainer "Christian Shaw"

WORKDIR /opt

COPY requirements.txt ./
COPY dist/docker-entrypoint.sh ./

RUN pip -qq install --upgrade pip
RUN pip -qq install -r requirements.txt

ENV LOCUSTFILE_PATH=/opt/locust/scripts/locustfile.py
ENV TARGET_URL=http://api.sauce-project.tech
# The mode can be either standalone, master or worker
ENV MODE=standalone

ENTRYPOINT ["./docker-entrypoint.sh"]
