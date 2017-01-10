#!/bin/bash

yum install epel-release -y
yum install certbot -y


if [ ! -f /etc/letsencrypt/renewal ]
  then
    certbot certonly --webroot -w /www -d {{cookiecutter.nginx_server_name}}
  else
    certbot renew --quiet
fi

