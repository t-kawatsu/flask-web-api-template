# vim:set ft=dockerfile:
FROM python:3.9

LABEL com.jogoj.service.name="app" \
      com.jogoj.service.type="app" \
      version="0.1" \
      description=""

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo
ENV APP_HOME=/usr/src/app \
    HOME=/root

# install poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH=$PATH:$HOME/.poetry/bin
RUN poetry self update 1.1.6 ;\
    poetry config cache-dir ${APP_HOME}/.cache/pypoetry ;\
    rm -rf ${HOME}/.cache/pypoetry

WORKDIR ${APP_HOME}

# SHELL ["/bin/bash", "-lc"]

EXPOSE 5000/tcp

CMD ["make", "run"]