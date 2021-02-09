from typing import List

import pytest
from pytest_cookies.plugin import Result

_DEPENDENCY_FILE = "pyproject.toml"
_MAKEFILE = "Makefile"
_PYTHON_VERSION_FILE = ".python-version"


@pytest.fixture
def context():
    return {
        "full_name": "Test User",
        "email": "test.user@testland.com",
        "project_name": "Test Bake Project",
        "project_description": "A test project with which to test."
    }


def test_bake(cookies, context):
    # given
    expected_dependencies = ['pytest', 'flake8', 'mypy', 'pre-commit']

    # when
    r: Result = cookies.bake(extra_context=context)
    top_level_files: List[str] = [f.basename for f in r.project.listdir()]

    # then
    assert r.exit_code == 0
    assert r.exception is None
    assert r.project.basename == "test-bake-project"
    assert all([dep in r.project.join(_DEPENDENCY_FILE).read() for dep in expected_dependencies])
    assert '.pre-commit-config.yaml' in top_level_files
    assert '.circleci' in top_level_files


def test_python_version(cookies, context):
    # given
    python_version = "3.8.5"
    context["python_version"] = python_version

    # when
    r: Result = cookies.bake(extra_context=context)

    # then
    assert r.exit_code == 0
    assert python_version in r.project.join(_DEPENDENCY_FILE).read()
    assert python_version in r.project.join(_PYTHON_VERSION_FILE).read()


def test_no_pre_commit(cookies, context):
    # given
    context["use_pre_commit"] = "n"

    # when
    r: Result = cookies.bake(extra_context=context)
    top_level_files: List[str] = [f.basename for f in r.project.listdir()]

    # then
    assert r.exit_code == 0
    assert '.pre-commit-config.yaml' not in top_level_files
    assert 'pre-commit' not in r.project.join(_DEPENDENCY_FILE).read()


def test_no_circle_ci(cookies, context):
    # given
    context["use_circle_ci"] = 'n'

    # when
    r: Result = cookies.bake(extra_context=context)
    top_level_files: List[str] = [f.basename for f in r.project.listdir()]

    # then
    assert r.exit_code == 0
    assert '.circleci' not in top_level_files


@pytest.mark.xfail
def test_email_validation(cookies, context):
    # given
    invalid_email = 'invalid@email@gmail.com'
    context["email"] = invalid_email

    # expecting, when
    with pytest.raises(Exception):
        cookies.bake(extra_context=context)
