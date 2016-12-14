__author__ = '{{cookiecutter.author }}'
import os
import ssl
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

appname = "{{cookiecutter.application_short_name }}" 
#****** Application Settings *******************************************************
Page_Title = 'API'
Application_Title = '{{cookiecutter.application_title }}'
#****** Django Settings  ***********************************************************

SECRET_KEY = '(This is a secret key. Update key to secure api)'
# SCRIPT_NAME Override, I had difficulty setting up NGINX settings
# proxy_set_header SCRIPT_NAME /api; # Not working in config. Temporary fix by add
# FORCE_SCRIPT_NAME in Django settings.py
# If None will default back to Nginx config.
FORCE_SCRIPT_NAME= '/api/'

#Behind reverse proxy set header to trust for https
#replace values in next two lines with commented text if https is needed and behind proxy
USE_X_FORWARDED_HOST = {% if cookiecutter.ssl_self_signed =='y' %}True{% else %}False  # True{% endif %}
SECURE_PROXY_SSL_HEADER = {% if cookiecutter.ssl_self_signed =='y' %}('HTTP_X_FORWARDED_PROTO', 'https'){% else %}None  # ('HTTP_X_FORWARDED_PROTO', 'https'){% endif %}

#NGINX EXAMPLE for https
#   location  /api/ {
#           add_header 'Access-Control-Allow-Origin' '*';
#           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
#           proxy_set_header Host $http_host;
#           proxy_set_header X-Forwarded-Proto 'https';
#           proxy_pass http://0.0.0.0:8080/ ;
#    }
# From above Access-Control-Allow-Origin is used to enable cross-orgin resource sharing(CORS)
# Many different configurations - 'Access-Control-Allow-Origin' '*' allows all hosts. Please
# check the docs depending on web server used. This example is for Nginx!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
# Cookie Domain
# Domain cookie. Can overide for subdomains ie. ".example.com"  (note the leading dot!)
# for cross-domain cookies, or use None for a standard domain cookie.
SESSION_COOKIE_DOMAIN =None
CSRF_COOKIE_DOMAIN = None

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASE_ROUTERS = []
#******* Queue  *******************************************************

MEMCACHE_HOST = "cybercom_memcache"
MEMCACHE_PORT = 11211

MONGO_HOST = "cybercom_mongo"
MONGO_PORT = 27017 
MONGO_DB = "{{cookiecutter.application_short_name }}"
MONGO_LOG_COLLECTION = "task_log"
MONGO_TOMBSTONE_COLLECTION = "tombstone"

BROKER_URL = 'amqp://{{cookiecutter.broker_user}}:{{cookiecutter.broker_pass}}@cybercom_rabbitmq:{{cookiecutter.broker_port}}/{{cookiecutter.broker_vhost}}'
BROKER_USE_SSL = {
  'keyfile': '/sslconf/client/key.pem',
  'certfile': '/sslconf/client/cert.pem',
  'ca_certs': '/sslconf/testca/cacert.pem',
  'cert_reqs': ssl.CERT_REQUIRED
}


CELERY_RESULT_BACKEND = "mongodb://cybercom_mongo:27017/"
CELERY_MONGODB_BACKEND_SETTINGS = {
    "database": MONGO_DB,
    "taskmeta_collection": MONGO_TOMBSTONE_COLLECTION
}

#******* Catalog ******************************************************
CATALOG_EXCLUDE = ['admin','local','cybercom_auth','system.users','default_collection','{{cookiecutter.application_short_name }}']
CATALOG_INCLUDE = ['catalog']
CATALOG_URI = 'mongodb://cybercom_mongo:27017/'
CATALOG_ANONYMOUS=True
#*********** Data Store ************************************************
DATA_STORE_EXCLUDE = ['admin','local','cybercom_auth','system.users','catalog','default_collection','{{cookiecutter.application_short_name }}',]
DATA_STORE_MONGO_URI = 'mongodb://cybercom_mongo:27017/'
DATA_STORE_ANONYMOUS=True
#*********** DOCKER_HOST_DATA_DIRECTORY ********************
DOCKER_HOST_DATA_DIRECTORY = "{{cookiecutter.docker_host_data_directory}}/{{cookiecutter.application_short_name }}"
