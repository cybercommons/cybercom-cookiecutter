__author__ = '{{ author }}'

#****** Application Settings *******************************************************
Page_Title = 'API'
Application_Title = '{{ application_title }}'
#****** Django Settings  ***********************************************************

SECRET_KEY = '(This is a secret key. Update key to secure api)'
# SCRIPT_NAME Override, I had difficulty setting up NGINX settings
# proxy_set_header SCRIPT_NAME /api; # Not working in config. Temporary fix by add 
# FORCE_SCRIPT_NAME in Django settings.py 
# If None will default back to Nginx config. 
# Provide custom config.py with docker cybercom/api
# docker run -v <path to config.py>:/usr/src/app/api/config.py cybercom/api
FORCE_SCRIPT_NAME='/api/'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
# Cookie Domain
# Domain cookie. Can overide for subdomains ie. ".example.com"  (note the leading dot!) 
# for cross-domain cookies, or use None for a standard domain cookie.
SESSION_COOKIE_DOMAIN = None
CSRF_COOKIE_DOMAIN = None

#******* Queue  *******************************************************
# This information must match the celeryconfig in the celery worker. If collections 
# are different data will not be available in api.
MEMCACHE_HOST = "127.0.0.1"
MEMCACHE_PORT = 11211

MONGO_HOST = '{{ mongo_host }}'
MONGO_PORT = {{ mongo_port }}
MONGO_DB = "{{ application_shortname }}"
MONGO_LOG_COLLECTION = "task_log"
MONGO_TOMBSTONE_COLLECTION = "tombstone"

BROKER_URL = 'pyamqp://{{broker_user}}:{{broker_pass}}@{{broker_host}}:{{broker_port}}/{{application_short_name}}'

CELERY_RESULT_BACKEND = "mongodb"
CELERY_MONGODB_BACKEND_SETTINGS = {
    "host": MONGO_HOST,
    "database": MONGO_DB,
    "taskmeta_collection": MONGO_TOMBSTONE_COLLECTION
}

#******* Catalog ******************************************************
# Default localhost
CATALOG_EXCLUDE = ['admin','local','cybercom_auth','system.users']
CATALOG_URI = 'mongodb://localhost:27017/'

#*********** Data Store ************************************************
# Default localhost
DATA_STORE_EXCLUDE = ['admin','local','cybercom_auth','system.users','cybercom_queue','df']
DATA_STORE_MONGO_URI = 'mongodb://{{mongo_host}}:{{mongo_port}}/'
