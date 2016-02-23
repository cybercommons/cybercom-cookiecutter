__author__ = '{{cookiecutter.author }}'

#****** Application Settings *******************************************************
Page_Title = 'API'
Application_Title = '{{cookiecutter.application_title }}'
#****** Django Settings  ***********************************************************

SECRET_KEY = '(This is a secret key. Update key to secure api)'
# SCRIPT_NAME Override, I had difficulty setting up NGINX settings
# proxy_set_header SCRIPT_NAME /api; # Not working in config. Temporary fix by add
# FORCE_SCRIPT_NAME in Django settings.py
# If None will default back to Nginx config.
# Provide custom config.py with docker cybercom/api
# docker run -v <path to config.py>:/usr/src/app/api/config.py cybercom/api

FORCE_SCRIPT_NAME= '/api/'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
# Cookie Domain
# Domain cookie. Can overide for subdomains ie. ".example.com"  (note the leading dot!)
# for cross-domain cookies, or use None for a standard domain cookie.
SESSION_COOKIE_DOMAIN =None
CSRF_COOKIE_DOMAIN = None
#http://head.ouetag.org/api/api-auth/login/?next=/api/
#******* Queue  *******************************************************

MEMCACHE_HOST = "{{cookiecutter.memcache_host}}"
MEMCACHE_PORT = {{cookiecutter.memcache_port}}

MONGO_HOST = '{{cookiecutter.mongo_host }}'
MONGO_PORT = {{cookiecutter.mongo_port}}
MONGO_DB = "{{cookiecutter.application_shortname }}"
MONGO_LOG_COLLECTION = "task_log"
MONGO_TOMBSTONE_COLLECTION = "tombstone"

BROKER_URL = 'amqp://{{cookiecutter.broker_user}}:{{cookiecutter.broker_pass}}@{{cookiecutter.broker_host}}:{{cookiecutter.broker_port}}/{{cookiecutter.broker_vhost}}'

CELERY_RESULT_BACKEND = "mongodb"
CELERY_MONGODB_BACKEND_SETTINGS = {
    "host": MONGO_HOST,
    "database": MONGO_DB,
    "taskmeta_collection": MONGO_TOMBSTONE_COLLECTION
}

#******* Catalog ******************************************************
CATALOG_EXCLUDE = ['admin','local','cybercom_auth','system.users','cybercom_queue','mgmic_queue','test']
CATALOG_URI = 'mongodb://{{cookiecutter.mongo_host }}:{{cookiecutter.mongo_port}}/'

#*********** Data Store ************************************************
DATA_STORE_EXCLUDE = ['admin','local','cybercom_auth','system.users','cybercom_queue']
DATA_STORE_MONGO_URI = 'mongodb://{{cookiecutter.mongo_host }}:{{cookiecutter.mongo_port}}/'
#*********** DOCKER_HOST_DATA_DIRECTORY ********************
DOCKER_HOST_DATA_DIRECTORY = "{{cookiecutter.docker_host_data_directory}}"
