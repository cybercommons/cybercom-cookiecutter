# All broker and mongo information must correspond to Celery Broker and REST API
# This is an example with no connections placed within this file. <variable_name> 
# Please use the single node cookiecutter and copy celery/code to make sure everything matches!
BROKER_URL = 'amqp://<broker_user>:<broker_password>@<broker_host>:<broker_port>/<broker_vhost>'
CELERY_SEND_EVENTS = True
CELERY_TASK_RESULT_EXPIRES = None
CELERY_ACCEPT_CONTENT = ['pickle','json']
CELERY_RESULT_BACKEND = "mongodb://<mongo_host>:<mongo_port>/"
CELERY_MONGODB_BACKEND_SETTINGS = {
    "database": "<application_short_name>",
    "taskmeta_collection": "tombstone"
}
#If you are pip installing the requirements.txt. It has the cybercomq repo. Example add task!
CELERY_IMPORTS = ("cybercomq",)
