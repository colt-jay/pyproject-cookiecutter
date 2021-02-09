VERSION_PYTHON := $(shell cat .python-version)

.PHONY: help init python
.DUMMY: help

help:
	@echo "You're doing great!"

init: python poetry {% if cookiecutter.use_pre_commit == 'y' %}pre-commit{% endif %}

python:
	@pyenv install --skip-existing ${VERSION_PYTHON}

poetry:
	@poetry install

{% if cookiecutter.use_pre_commit == 'y' %}
pre-commit:
	@poetry run pre-commit install

update-hooks:
	@poetry run pre-commit autoupdate

{% endif %}

clean:
	@rm -rf temp .mypy_cache .pytest_cache
