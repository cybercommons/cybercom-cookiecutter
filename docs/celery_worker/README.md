### Cybercommons Celery Asynchronous Queue

[Celery](http://www.celeryproject.org/) is an asynchronous task queue/job queue based on distributed message passing. It is focused on real-time operation, but supports scheduling as well.

The execution units, called tasks, are executed concurrently on a single or more worker servers using multiprocessing, Eventlet, or gevent. Tasks can execute asynchronously (in the background) or synchronously (wait until ready).

##### Celery Worker node deployment

1. Python Virtual Environment 
	
	__Requirements__
	
	* PIP - [Install](https://packaging.python.org/en/latest/install_requirements_linux/#installing-pip-setuptools-wheel-with-linux-package-managers)
	
	__Install__
	
	1. Virtual Environment
	
	        $ pip install virtualenv
	
	2. Get Celery Config and Requirements
	
	         
	         
	         $ wget -r --no-parent https://github.com/cybercommons/cybercom-cookiecutter/blob/master/%7B%7Bcookiecutter.application_short_name%7D%7D/celery/code