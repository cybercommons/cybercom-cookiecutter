import os
appname = "{{cookiecutter.application_short_name}}"
BROKER_URL = 'amqp://{{cookiecutter.broker_user}}:{{cookiecutter.broker_pass}}@cybercom_rabbitmq:{{cookiecutter.broker_port}}/{{cookiecutter.broker_vhost}}'
CELERY_SEND_EVENTS = True
CELERY_TASK_RESULT_EXPIRES = None
CELERY_ACCEPT_CONTENT = ['pickle','json']
CELERY_RESULT_BACKEND = "mongodb://cybercom_mongo:27017/"
CELERY_MONGODB_BACKEND_SETTINGS = {
    "database": "{{cookiecutter.application_short_name}}",
    "taskmeta_collection": "tombstone"
}
CELERY_IMPORTS = ("{{cookiecutter.queue_tasks_repo}}",)
