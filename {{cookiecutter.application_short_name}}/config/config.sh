# Broker (rabbitmq) configs 
vhost={{cookiecutter.broker_vhost}}
broker_username={{cookiecutter.broker_user}}
broker_password={{cookiecutter.broker_pass}}
tag={{cookiecutter.application_short_name}}

# path to Nginx SSL keys
ssl_key_path={{cookiecutter.application_install_directory}}/{{cookiecutter.application_short_name}}/config/ssl/nginx/keys/selfsigned.key
ssl_cert_path={{cookiecutter.application_install_directory}}/{{cookiecutter.application_short_name}}/config/ssl/nginx/keys/selfsigned.crt
ssl_dhparam_path={{cookiecutter.application_install_directory}}/{{cookiecutter.application_short_name}}/config/ssl/nginx/keys/dhparam.pem

# Mongodb - mongo URI fields in apiconfig.py and celeryconfig.py will need to be manually updated to match
mongo_username={{cookiecutter.broker_user}}
mongo_password={{cookiecutter.broker_pass}}

# uncomment and populate the following two lines for the resetDBCreds application to add / update the mongo user admin account
#mongo_admin_username=
#mongo_admin_password=
#mongo_admin_role=root
