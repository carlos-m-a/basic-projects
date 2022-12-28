# Django REST framework (DRF) basic project

## Description

Django API REST project for quick start.

The  apps of this projects are:
* app1: Simple example app about to-dos and notes for showing the different types of views in DRF

## Installation

* Clone this repository
* Create a virtual environment (e.g.:'venv' with virtualenv)
* Create a database in your local RDBMS for this project
* Create a '.env' from 'env-variables-example.txt', in the same folder that 'settings.py', and fill every single field with your local-custom data
* Install every package in requeriments.txt (pip install -r requeriments.txt)
* python manage.py makemigrations
* python manage.py migrate
* (for production) python manage.py collectstatic
