#!/bin/bash

pip install pipenv

pipenv install

pipenv shell

pip install django

python manage.py migrate

python manage.py runserver
