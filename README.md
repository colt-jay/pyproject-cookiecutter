# Python Project Cookiecutter [![colt-jay](https://circleci.com/gh/colt-jay/pyproject-cookiecutter.svg?style=svg)](https://app.circleci.com/pipelines/github/colt-jay/pyproject-cookiecutter)

🐍🍪 An opinionated template for streamlining python project creation.

## Usage

### Creating A New Project

```bash
brew install pyenv
pip install -U cookiecutter
cookiecutter gh:colt-jay/pyproject-cookiecutter
```

### Initializing Your New Project

```bash
# Install System Tooling
brew install pyenv
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# Initialize Project Env
make init
```

## Tooling

This template utilizes the following tools.

- Python Interpreter: [`pyenv`](https://github.com/pyenv/pyenv) + `.python-version`
- Python VirtualEnv & Dependency Resolution: [`poetry`](https://github.com/python-poetry/poetry) + `pyproject.toml`
- Linting: [`flake8`](https://github.com/PyCQA/flake8) + [`mypy`](https://github.com/python/mypy) + `setup.cfg`
- Testing: [`pytest`](https://github.com/pytest-dev/pytest)
- (optional) Standards Enforcement: [`pre-commit`](https://github.com/pre-commit/pre-commit) + `.pre-commit-config.yaml`
- (optional) Continuous Integration: [CircleCi](https://circleci.com/docs/) + `.circleci/config.yml`
- Project Tooling: `make` + `Makefile`
