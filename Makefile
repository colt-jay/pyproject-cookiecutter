VERSION_PYTHON := $(shell cat .python-version)

.PHONY: help init python
.DUMMY: help

help:
	@echo "You're doing great!"

init: python poetry pre-commit

python:
	@pyenv install --skip-existing ${VERSION_PYTHON}

poetry:
	@poetry install

pre-commit:
	@poetry run pre-commit install

update-hooks:
	@poetry run pre-commit autoupdate

test:
	@poetry run pytest tests/

gen:
	@poetry run cookiecutter -o temp .

clean:
	@rm -rf temp .mypy_cache .pytest_cache
