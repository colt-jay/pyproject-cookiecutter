import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(dirpath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, dirpath))


if __name__ == '__main__':
    if '{{ cookiecutter.use_pre_commit }}' != 'y':
        remove_file('.pre-commit-config.yaml')

    if '{{ cookiecutter.use_circle_ci }}' != 'y':
        remove_dir('.circleci')
