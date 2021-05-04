======================
flask-web-api-template
======================

This is the template repository for flask web-api applications that are constructed with Docker.


Stack
-----
- Python 3.9
- Docker
- Poetry
- MySQL 8.0
- Make


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

