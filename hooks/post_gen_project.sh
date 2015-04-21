#!/bin/sh
git clone https://github.com/ouinformatics/restful-api-application-template client/
git clone https://github.com/ouinformatics/restful-api api # -v /api /usr/src/app (for api container)
mv -f api_config.py api/api/config.py
git clone --recursive -b cookiecutter https://github.com/ouinformatics/risser-docker docker
mv config/rabbitmq_config.sh docker/rabbitmq/config.sh

docker/build.sh

