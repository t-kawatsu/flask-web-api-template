======================
flask-web-api-template
======================

.. image:: https://github.com/t-kawatsu/flask-web-api-template/actions/workflows/test.yml/badge.svg

This is the template repository for flask web-api applications that are constructed with Docker.


Stack
-----
- Python 3.9
- Docker
- Poetry
- MySQL 8.0
- Make
- Github Actions ( CI / CD tool )


Requirements
------------
- Docker

You need a runtime that installed docker machine for building.


Development
-----------
.. code-block:: bash

  $ docker-compose build

  $ cp .env.sample .env

  $ docker-compose up

  # Setup app
  $ make setup

  # Lint
  $ make lint

  # Test
  $ make test

  # Build
  $ make build

  # Run
  $ make run


API
---

OpenAPI_.

.. _OpenAPI: docs/openapi.yml


Troubleshooting
---------------


Lisence
-------

