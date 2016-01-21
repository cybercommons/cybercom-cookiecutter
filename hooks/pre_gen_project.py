import os
from cookiecutter.main import cookiecutter
from os.path import expanduser

home = expanduser("~")

current_dir =  os.getcwd() #os.path.dirname(os.path.realpath(__file__))
print current_dir
cookiecutter('risser-cookiecutter',
             extra_context={'docker_host_data_directory':current_dir,'user_home':home})
