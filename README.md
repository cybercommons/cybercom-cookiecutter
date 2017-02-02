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
├── api_code (Github Repository https://github.com/cybercommons/cybercom-api)
├── config
│   ├── addmongouser
│   ├── api_config.py
│   ├── celery
│   │   └── code
│   │       ├── celeryconfig.py
│   │       ├── celeryconfig.pyc
│   │       └── requirements.txt
│   ├── config.sh
│   ├── db.sqlite3 (Database of API users, permissions, and group settings)
│   ├── nginx (Configuration related files)
│   └── ssl
│       ├── backend
│       │   ├── ca.conf
│       │   ├── client (Generated client side certificates)
│       │   ├── generate
│       │   ├── keystoresecret
│       │   ├── server (Generated server side certificates)
│       │   └── testca (Generated CA files used to sign client and server side certifictes)
│       └── nginx
│           ├── generate
│           ├── keys (generated dhparam and self signed certificates)
│           ├── letsencrypt
│           │   ├── dockerfiles (Files used to generate Docker container)
│           │   ├── etc (Let's Encrypt working files and generated certificates)
│           │   ├── nginx-bootstrap.conf
│           │   └── www (Working path for Let's Encrypt's .well-known/acme-challenge)
│           └── runLetsEncrypt
├── data
│   ├── local
│   │   └── static
│   │       └── api (REST API CSS Content)
│   ├── mongo (MongoDB data folder)
│   └── static (Web Accessible Directory)
│       └── portal (Github Repository https://github.com/cybercommons/cybercom-portal)
├── log
│   ├── api.log
│   └── celery.log
└── run
    ├── appContainerKill
    ├── cybercom_up
    ├── genSSLKeys
    └── resetDBCreds
```
###1) Install Cybercommons Configuration 

	$ cookiecutter https://github.com/cybercommons/cybercom-cookiecutter.git
 

Cookiecutter Questions: Can enter information or press enter for default value.

Author and Application Title: 

	author [Some Guy]: 
	application_title [Some Application]:

Application Short Name will be a directory name. DO NOT include spaces or illegal characters within short name.


	application_short_name [someapp]: 

	
Nginx Server Name is the URL for the web server - default is to use "localhost"

	nginx_server_name [localhost]:	

Use SSL allows for settings up Secure HTTP (HTTPS) connections to the Nginx webserver - default is to not enable HTTPS. SSL Valid Days is used to set certificate expirations for MongoDB, RabbitMQ, and self-signed certificates. The default is set to 1 year. This expiration setting does not impact Let's Encrypt created certificates.

	use_ssl [1 - None, 2 - LetsEncrypt, 3 - SelfSeigned]
	ssl_valid_days [365]:
	
RabbitMQ: Broker Default host and ports - Message broker virtual host, username, and password.
	
	broker_host [localhost]:
	broker_port [5672]:
	broker_vhost [vhost]:
	broker_user [quser]:
	broker_pass [qpass]:

Queue Tasks: Github Organization, Repo, and Branch. Default will give you generic tasks with test add task.

	queue_tasks_org [cybercommons]:
	queue_tasks_repo [cybercomq]:
	queue_tasks_branch [master]:
	
Celery Concurrency: The number of concurrent tasks that can run simultaneously.  

	celery_concurrency [8]:

Docker: The docker_worker and docker_username are only used when celery tasks are going to create a sister/brother docker container. This is configured in cybercom_up file in the run directory. The docker_worker is the host where the docker container will be created. The docker_username is a user with ssh keys and has privledges to run docker commands. ssh keys are not setup and must be done to allow ssh to docker worker.
	
	docker_worker [example.oscer.ou.edu]:
	docker_username [mstacy]:

Application Install Directory: This is a work around for finding the current application install directory (install location). CookieCutter does have this capability, but for some reason could not figure out how to set an additional template parameter or access within template.

	application_install_directory [/opt]:
	

###2) Build API Docker Container

	$ cd someapp/api_code
	$ docker build -t api .
	$ cd ..
	 
###3) Build Let's Encrypt Docker Container
If Let's Encrypt was selected during step 1, run the following commands to build its container.

    $ cd someapp/config/ssl/nginx/letsencrypt/dockerfiles
    $ docker build -t certbot .
    $ cd ../../
    $ ./runLetsEncrypt
        
The runLetsEncrypt script can be manually executed to renew expired certificates or added to a cron job.

###4) Run CyberCommons Platform

	$ ./run/cybercom_up
	
###5) Successful Installation 

	$ docker ps
	
	CONTAINER ID    IMAGE            COMMAND                  (Trimmed Output)                                                           
	8586e51e37a4    nginx            "nginx -g 'daemon off"                                                
	c7ee4754a2fc    api              "gunicorn --config=gu"
	cca72df2e81f    memcached        "/entrypoint.sh me..."   
	364d90b9e7e3    cybercom/celery  "/run.sh" 
	12dba22cf2a9    rabbitmq         "/docker-entrypoint.s"
	b7e6efd64e33    mongo            "/entrypoint.sh mongo"  	

###### Check Application
1. Web Access __http://<< nginx_server_name >>/__
2. Example portal application with add task  __http://<< nginx_server_name >>/portal__
3. RESTful API  __http://<< nginx_server_name >>/api/__


#####5) RESTful API and Portal Default User

	username: admin
	password: admin
	
