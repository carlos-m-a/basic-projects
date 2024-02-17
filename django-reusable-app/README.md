# django-reusable-app

This is a example of a project with the structure ready for create a Django reusable app. You can just copy-paste this app folders/files, and change the name of the app (now: reusable_app) in every folder/file where it appears.


## How to use this repo as a template

1. Clone this repo
2. Remove the .git folder
3. Change repo name and app name
4. In wrapper/settings.py, change INSTALLED_APPS: reusable_app -> new_app_name
5. In wrapper/urls.py, change: reusable_app -> new_app_name
6. Inside new_app_name folder, remember to change the app name variable in apps.py and urls.py
6. git init .
7. Remember modify pyproject.toml with your new repo name and app name


## How to run using Docker

Docker files (Dockerfile, docker-compose.yml, .env.dev) are ready to use.

To run the containers: `docker compose up -d --build`

Now wait and go to http://localhost:8000/reusable_app/my_model_list/ to check if it runs correctly.

To stop and remove everything: `docker compose down -v --rmi "local"`

To stop and don't remove the data in the database for the next compose up: `docker compose down --rmi "local"`

That's it, docker makes things easy.

## Quick start to develop

1. Install requirements using pip (Remember to create you virtual environment):

    pip install -r requirements.txt

2. Copy-paste env-variables-example.txt inside "wrapper" folder, and change the name to ".env"

3. Edit ".env" file, adapting it to your local context

4. Run  ``python manage.py makemigrations`` and ``python manage.py migrate`` to create the tables in the data base.

5. Start the development server and visit this link (http://127.0.0.1:8000/auth/login/) to check everything is running ok.


## How to add this app inside your Django project as a git submodule

Add this repository in you `.gitmodules` file, like this: 
```git
[submodule "reusable_app"]
	path = path/to/external/apps
	url = https://github.com/username/django-reusable-app
    branch = master
```

You can create a soft link to the app folder.
Inside the same folder where `manage.py` is, do this (linux):
```bash
ln -s path/to/external/apps/django-reusable-app/reusable_app reusable_app
```

Remember to modify the next files: 

In `settings.py`:
```python
INSTALLED_APPS = (
    "reusable_app",
    # If you did't create a soft link, use this:
    #"django-reusable-app.reusable_app",
)
```

In `urls.py`:
```python
urlpatterns = [
    path("reusable_app/", include(reusable_app)),
    # If you didn't create a soft link, use this:
    #path("reusable_app/", include(django-reusable-app.reusable_app)),

]
```


## How to generate a python package using a build system (And import to django)

Since this repo only uses the `pyproject.toml`, remember to use at least the version 61.0.0 of setuptools, or other package managers or build systems like hatchling, poetry, etc., that only needs `pyproject.toml`. (Modern python packers only needs pyproject.toml, there is no need of setup.py or setup.cfg) 

Remember to modify `pyproject.toml`, remplacing data for your package data. The file is prepared to be used by "setuptools" library. If you want to use other build system, remember to edit the `[build-system]` part.

For building the package (setuptools):
```bash
python -m pip install --upgrade setuptools
python -m pip install --upgrade setuptools wheel
python -m build
python -m pip install --user dist/django-reusable-app-0.0.1.tar.gz
```


## Quick start to use in your project when you packed this project

Fist you need to check the section "How to generate a python package using a build system"

1. Install the app (you need a dist version of the app, "django-reusable-app" is just an example):

    pip install django-reusable-app
    
    or

    python -m pip install --user dist/django-reusable-app-0.0.1.tar.gz

2. Add "reusable_app" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'reusable_app',
        ...
    ]

3. Include the polls URLconf in your project urls.py like this::

    path('reusable_app/', include('reusable_app.urls')),

4. Run  ``python manage.py makemigrations`` and ``python manage.py migrate`` to create the tables in the data base.

5. Start the development server and visit this link (http://127.0.0.1:8000/auth/login/) to check everything is running ok.