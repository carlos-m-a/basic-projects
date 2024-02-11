# django-reusable-app

This is a example of a project with the structure ready for create a Django reusable app. You can just copy-paste this app folders/files, and change the name of the app (now: reusable_app) in every folder/file where it appears.

## Quick start to use / develop

1. Install requirements using pip:

    pip install -r requirements.txt

2. Add "reusable_app" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'reusable_app',
        ...
    ]

3. Include the polls URLconf in your project urls.py like this::

    path('reusable_app/', include('reusable_app.urls')),

4. Run  ``python manage.py makemigrations`` and ``python manage.py migrate`` to create the tables in the data base.

5. Start the development server and visit admin site (e.g. http://127.0.0.1:8000/admin/) to create a voting (you'll need the Admin app enabled).


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


## How to generate a package using a build system (And import to django)

Since this repo only uses the `pyproject.toml`, remember to use at least the version 61.0.0 of setuptools, or other package managers or build systems like hatchling, poetry, etc., that only needs `pyproject.toml`. (Modern python packers only needs pyproject.toml, there is no need of setup.py or setup.cfg) 

Remember to modify `pyproject.toml`, remplacing data for your package data. The file is prepared to be used by "setuptools" library. If you want to use other build system, remember to edit the `[build-system]` part.

For building the package:
```bash
python -m build
```