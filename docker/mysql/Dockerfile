# vim:set ft=dockerfile:
FROM mysql:8.0

LABEL com.jogoj.service.name="mysql" \
      com.jogoj.service.type="mysql" \
      version="0.1" \
      description=""

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

COPY conf.d/my.cnf /etc/mysql/conf.d

# It will execute files with extensions .sh, .sql and .sql.gz that are found in /docker-entrypoint-initdb.d.
# Files will be executed in alphabetical order
COPY initdb.d/* docker-entrypoint-initdb.d

EXPOSE 3306/tcp
