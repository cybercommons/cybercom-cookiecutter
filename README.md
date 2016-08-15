Cybercommons Cookiecutter
========================

This repo uses cookiecutter to install the cyberCommons platform on a single node. The cybercommons platform is a microservice architecture that provides a RESTful API (Django REST Framework) , Data Catalog(MongoDB), and Asyncronous workflow system (Celery).

### Installation

##### Dependencies Requirements

1. Docker
    * [Docker Install Documentation](https://docs.docker.com/engine/installation/)
2. CookieCutter
    * pip install cookiecutter

##### CookieCutter
Cookiecutter creates the following file structures:

```
.
├── api_code (Github Repository https://github.com/cybercommons/cybercom-api)
├── celery
│   ├── code
│   │   ├── celeryconfig.py
│   │   └── requirements.txt
│   └── log
│       └── celery.log
├── config
│   ├── api_config.py
│   └── db.sqlite3
├── data
│   ├── api_log
│   │   └── api.log
│   ├── mongo (MongoDB data folder)
│   ├── local
│   │   └── static
│   │       └── api (REST API CSS Content)
│   └── static
│       └── portal (Github Repository https://github.com/cybercommons/cybercom-portal)
├── nginx
│   ├── default.conf
│   └── nginx.conf
└── run
    ├── config.sh
    ├── docker_restart (Kills all running Docker Container; Uncomment or add docker restart based on Linux Distro)
    └── cybercom_up (Starts single node cyberCommons platform)
```
######1) Install Cybercommons Configuration 

	$ cookiecutter https://github.com/cybercommons/cybercom-cookiecutter.git
 

Cookiecutter Questions: Can enter information or press enter for default value.

	author [Some Guy]: 
	application_title [Some Application]:
	application_short_name [someapp]: 

Application Short Name will be a directory name. DO NOT include spaces or illegal characters within short name.
	
	memcache_host [127.0.0.1]:
	memcache_port [11211]:

Memchache: Default host and port!	

	mongo_host [localhost]:
	mongo_port [27017]:
	
MongoDB: Default host and port
	
	broker_host [localhost]:
	broker_port [5672]:
	broker_vhost [vhost]:
	broker_user [quser]:
	broker_pass [qpass]:

RabbitMQ: Broker Default host and ports - Message broker virtual host, username, and password.

	queue_tasks_org [cybercommons]:
	queue_tasks_repo [cybercomq]:
	queue_tasks_branch [master]:
	
Queue Tasks: Github Organization, Repo, and Brach. Default will give you generic tasks with test add task. 

	celery_concurrency [8]:

Celery Concurrency
	
	docker_worker [example.oscer.ou.edu]:
	docker_username [mstacy]:

Docker: The docker_worker and docker_username are only used when celery tasks are going to create a sister/brother docker container to execute task. docker_worker is where the docker container will be created. The docker_username is a user with ssh keys and has privledges to run docker command. ssh keys are not setup and must be done to allow ssh to docker worker.
	
	docker_host_data_directory [/opt]:
	
Docker Host Data Directory: This is a work around for the current install directory of cookiecutter. CookieCutter does have this capability, but for some reason could not figure out how to set an additional template parameter or access within template.

######2) Build API Docker Container

	$ cd someapp/api_code
	$ docker build -t api .
	$ cd ..
	 
######3) Run CyberCommons Platform

	$ ./run/cybercom_up
	
#####4) Successful Installation 

	$ docker ps
	
	CONTAINER ID    IMAGE            COMMAND                  (Trimmed Output)                                                           
	8586e51e37a4    nginx            "nginx -g 'daemon off"                                                
	c7ee4754a2fc    api              "gunicorn --config=gu"   
	364d90b9e7e3    cybercom/celery  "/run.sh" 
	12dba22cf2a9    rabbitmq         "/docker-entrypoint.s"
	b7e6efd64e33    mongo            "/entrypoint.sh mongo"  	

__Navigate to http://<< host >>/ or http://<< host >>/portal or http://<< host >>/api/__

If install performed on Mac OSX system. Make sure your perform cookiecutter within your home directory. Virtualbox setup can only share directories within your home directory. Plus need to find ip address of virtualbox host. *__$ docker-machine ip default__*

#####5) RESTful API and Portal Default User

	username: admin
	password: admin
	
