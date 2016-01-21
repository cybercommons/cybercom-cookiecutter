import os
from cookiecutter.main import cookiecutter
from os.path import expanduser

home = expanduser("~")

current_dir = os.path.dirname(os.path.realpath(__file__))
cookiecutter('cookiecutter-pypackage/',
             extra_context={'docker_host_data_directory':current_dir,'user_home':home})
