.PHONY: help init test requirements clean
.DUMMY: help

VERSION_PYTHON := $(shell cat .python-version)

help:
	@echo "You're doing great!"

init:
	@pyenv install --skip-existing ${VERSION_PYTHON}
	@poetry install
{% if cookiecutter.use_pre_commit == 'y' %}
	@poetry run pre-commit install

update-hooks:
	@poetry run pre-commit autoupdate
{% endif %}

test:
	@poetry run pytest tests/

requirements:
	@poetry export --format=requirements.txt --output=requirements.txt --without-hashes

clean:
	@rm -rf temp .mypy_cache .pytest_cache
