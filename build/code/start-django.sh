#!/bin/sh

/code/manage.py makemigrations *insert app name here*
python /code/manage.py migrate
python /code/manage.py runserver 0.0.0.0:8080