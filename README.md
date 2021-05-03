# python-app-template

## Overview


## Stack

- Python 3.9
- Poetry ( is included in the docker )
- Docker


## development


### Requirements
- Docker


### Build dev Docker image & Run
```
# Build
$ docker build -t [YOUR APP NAME]-dev/app docker/
$ docker run --rm -it -v `pwd`:/usr/src/app [YOUR APP NAME]-dev/app make setup

# Run
$ docker run --rm -it -v `pwd`:/usr/src/app [YOUR APP NAME]-dev/app
```


## deployment


## How to


## Troubleshooting

