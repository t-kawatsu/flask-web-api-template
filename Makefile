setup: clean
	poetry install

build:
	poetry build

run:
	poetry run flask run --host 0.0.0.0

clean:
	rm -rf ./dist

lint:
	poetry run flake8

test:
	poetry run pytest
