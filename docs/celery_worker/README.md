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
	
	         
	         
	         $ wget https://raw.githubusercontent.com/cybercommons/cybercom-cookiecutter/master/docs/celery_worker/celeryconfig.py
            $ wget https://raw.githubusercontent.com/cybercommons/cybercom-cookiecutter/master/docs/celery_worker/requirements.txt 


    3. Update celeryconfig (replace <variables> with appropriate input.)
    4. Activate virtual environment

                $ source /path/to/virtualenv/bin/activate
                $ pip install -r requirements.txt

    4. Start Celery Worker(run in foreground) 

                $ celery worker -l info -Q etag -n dev-mstacy1

    5. Create bash script to run in backgroud

        See example code above (example_celery_up.sh)         

