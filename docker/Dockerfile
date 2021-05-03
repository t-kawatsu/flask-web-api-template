# vim:set ft=dockerfile:
FROM python:3.9

ENV TZ=Asia/Tokyo \
    LANG=ja_JP.UTF-8 \
    APP_HOME=/usr/src/app \
    HOME=/root

# install poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH=$PATH:$HOME/.poetry/bin
RUN poetry self update 1.1.6 ;\
    poetry config cache-dir ${APP_HOME}/.cache/pypoetry ;\
    rm -rf ${HOME}/.cache/pypoetry

WORKDIR ${APP_HOME}

# SHELL ["/bin/bash", "-lc"]

# EXPOSE 3000/tcp

# CMD ["python"]