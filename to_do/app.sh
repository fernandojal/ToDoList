#!/bin/bash

pip install pipenv

pipenv install

pipenv run pip install django

pipenv run python manage.py migrate

pipenv run python manage.py runserver
