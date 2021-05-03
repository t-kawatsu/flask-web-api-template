# vim:set ft=dockerfile:
FROM nginx:1.20

LABEL com.jogoj.service.name="nginx" \
      com.jogoj.type="nginx" \
      version="0.1" \
      description=""

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

RUN mkdir /etc/nginx/certs

COPY conf.d /etc/nginx/conf.d
COPY certs /etc/nginx/certs
