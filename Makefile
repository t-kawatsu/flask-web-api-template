setup: clean
	poetry install

build:
	poetry build

run:
	poetry run

clean:
	rm -rf ./dist

lint:
	poetry run flake8

test:
	poetry run pytest
