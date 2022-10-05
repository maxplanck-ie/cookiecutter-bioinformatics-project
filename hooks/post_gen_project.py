# credit to: https://github.com/cookiecutter/cookiecutter/issues/723

import os
import shutil


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

#provide_dockerfile = '{{cookiecutter.provide_dockerfile}}' == 'yes'

#if not provide_dockerfile:
    # remove top-level file inside the generated folder
    # remove('Dockerfile')
