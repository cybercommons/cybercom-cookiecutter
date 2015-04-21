#!/bin/sh
git clone https://github.com/ouinformatics/restful-api-application-template client/
git clone https://github.com/ouinformatics/restful-api /api # -v /api /usr/src/app (for api container)
mv -f api_config.py api/api/config.py
