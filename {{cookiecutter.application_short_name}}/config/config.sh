# Broker (rabbitmq) configs 
vhost={{cookiecutter.broker_vhost}}
user={{cookiecutter.broker_user}}
password={{cookiecutter.broker_pass}}
tag={{cookiecutter.application_short_name}}

# path to Nginx SSL keys
ssl_key_path={{cookiecutter.docker_host_data_directory}}/{{cookiecutter.application_short_name}}/config/ssl/nginx/keys/selfsigned.key
ssl_cert_path={{cookiecutter.docker_host_data_directory}}/{{cookiecutter.application_short_name}}/config/ssl/nginx/keys/selfsigned.crt
ssl_dhparam_path={{cookiecutter.docker_host_data_directory}}/{{cookiecutter.application_short_name}}/config/ssl/nginx/keys/dhparam.pem
