import os
from cookiecutter.main import cookiecutter
from os.path import expanduser

home = expanduser("~")

current_dir =  os.getcwd() #os.path.dirname(os.path.realpath(__file__))
print current_dir
#module_name = '{{ cookiecutter.module_name }}'
cookiecutter(os.path.join(home,'.cookiecutters/risser-cookiecutter/'),
             extra_context={'docker_host_data_directory':current_dir,'user_home':home})
