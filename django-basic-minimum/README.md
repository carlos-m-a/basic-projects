# Django basic minimum project

## Description

Minimum django project for quick starts.
It contains a basic accounts app and the 'base' app. Both use the default django utilities and cofigurations for authentication and basic templates to extend.

Accounts app handles every authentication use case and the updatings of user accounts. Since it uses django auth and it doesn't change django.auth operation, note that:
* In users, username is unique, but email don't. So differents users can have the same email
* That means users only can login with the username
* There isn't any limit to login attemps
* There isn't any email address verification by mail in the registration. Neither in the email updating.

The  apps of this projects are:
* accounts: manage every authentication use case. Don't modify
* base: for every base template to extend. Don't modify (only 'home')
* app1: example of extra app. remove it and create your own apps

## Installation

* Clone this repository
* Create a virtual environment (e.g.:'venv' with virtualenv)
* Create a database in your local RDBMS for this project
* Create a '.env' from 'env-variables-example.txt', in the same folder that 'settings.py', and fill every single field with your local/custom data
* Install every package in requeriments.txt (pip install -r requeriments.txt)
* python manage.py makemigrations
* python manage.py migrate
