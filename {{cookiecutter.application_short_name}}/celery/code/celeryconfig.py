import os
appname = "{{cookiecutter.application_short_name}}"
BROKER_URL = 'amqp://{{cookiecutter.broker_user}}:{{cookiecutter.broker_pass}}@{0}:{{cookiecutter.broker_port}}/{{cookiecutter.broker_vhost}}'
BROKER_URL = BROKER_URL.format(os.environ["{0}_RABBITMQ_PORT_5672_TCP_ADDR".format(appname.upper())])
CELERY_SEND_EVENTS = True
CELERY_TASK_RESULT_EXPIRES = None
CELERY_ACCEPT_CONTENT = ['pickle','json']
CELERY_RESULT_BACKEND = "mongodb://{0}:{{cookiecutter.mongo_port}}/"
CELERY_RESULT_BACKEND =CELERY_RESULT_BACKEND.format(os.environ["{0}_MONGO_PORT_27017_TCP_ADDR".format(appname.upper())])
CELERY_MONGODB_BACKEND_SETTINGS = {
    "database": "{{cookiecutter.application_short_name}}",
    "taskmeta_collection": "tombstone"
}
CELERY_IMPORTS = ("{{cookiecutter.queue_tasks_repo}}",)
