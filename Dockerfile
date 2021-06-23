FROM python:slim

LABEL maintainer="mahya safi <fateme.safi92@gmail.com>"

EXPOSE 8080

WORKDIR /opt/app

ENV	SKOB_AUTHZ_BIND_ADDRESS=0.0.0.0
ENV	SKOB_AUTHZ_NUM_WORKERS=4

COPY requirement.txt .
RUN pip install -r requirement.txt

COPY . .

RUN useradd -M -d /opt/app authz
USER authz:authz

CMD ./start
