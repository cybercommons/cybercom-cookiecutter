Cybercommons Cookiecutter
========================

This repo uses cookiecutter to install the cyberCommons platform on a single node. The cybercommons platform is a microservice architecture that provides a RESTful API (Django REST Framework) , Data Catalog(MongoDB), and Asyncronous workflow system (Celery).

cookiecutter creates the following file structures:

```
.
├── api_code (Github Repository https://github.com/cybercommons/cybercom-api)
├── celery
│   ├── code
│   │   ├── celeryconfig.py
│   │   ├── celeryconfig.pyc
│   │   └── requirements.txt
│   └── log
│       └── celery.log
├── config
│   ├── api_config.py
│   └── db.sqlite3
├── data
│   ├── api_log
│   │   └── api.log
│   ├── local
│   │   └── static
│   │       └── api (REST API CSS Content)
│   └── static
│       └── portal (Github Repository https://github.com/cybercommons/cybercom-portal)
├── mongo
│   └── _
├── nginx
│   ├── default.conf
│   └── nginx.conf
└── risser
    ├── config.sh
    ├── docker_restart
    └── risser_up
```