BROKER_URL = 'amqp://{{broker_user}}:{{broker_password}}@{{broker_host}}:{{broker_port}}/{{broker_vhost}}'
CELERY_SEND_EVENTS = True
CELERY_TASK_RESULT_EXPIRES = None
CELERY_ACCEPT_CONTENT = ['pickle','json']
CELERY_RESULT_BACKEND = "mongodb"
CELERY_MONGODB_BACKEND_SETTINGS = {
    "host": "{{mongo_host}}",
    "database": "{{application_short_name}}",
    "taskmeta_collection": "tombstone"
}
CELERY_IMPORTS = ("{{queue_tasks_repo}}",)
