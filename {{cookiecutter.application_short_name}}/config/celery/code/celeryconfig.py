import os
import ssl
appname = "{{cookiecutter.application_short_name}}"
BROKER_URL = 'amqp://{{cookiecutter.broker_user}}:{{cookiecutter.broker_pass}}@cybercom_rabbitmq:{{cookiecutter.broker_port}}/{{cookiecutter.broker_vhost}}'
BROKER_USE_SSL = {
  'keyfile': '/sslconf/client/key.pem',
  'certfile': '/sslconf/client/cert.pem',
  'ca_certs': '/sslconf/testca/cacert.pem',
  'cert_reqs': ssl.CERT_REQUIRED
}
CELERY_SEND_EVENTS = True
CELERY_TASK_RESULT_EXPIRES = None
CELERY_ACCEPT_CONTENT = ['pickle','json']
CELERY_RESULT_BACKEND = "mongodb://{{cookiecutter.broker_user}}:{{cookiecutter.broker_pass}}@cybercom_mongo:27017/?ssl=true&ssl_cert_reqs=CERT_NONE"
CELERY_MONGODB_BACKEND_SETTINGS = {
    "database": "{{cookiecutter.application_short_name}}",
    "taskmeta_collection": "tombstone"
}
CELERY_IMPORTS = ("{{cookiecutter.queue_tasks_repo}}",)
