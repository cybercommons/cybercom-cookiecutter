#!/bin/bash

yum install epel-release -y
yum install certbot -y


if [ ! -f /etc/letsencrypt/renewal ]
  then
    certbot certonly --webroot -w /www -d cc.lib.ou.edu
  else
    certbot renew --quiet
fi

