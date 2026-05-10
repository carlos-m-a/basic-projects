# Python Basic Project Structure

## Keep in mind:

* You should edit repository name (`python-basic`) and  project's folder name (`app_name`) with your custom project name (e.g.: `cars-manager` and `cars_manager`). Adapt every file to these changes.
* Your new code must be under `/app_name`. Create every new package there, and modify 'main' package code as well (but don't change the name of `main` package, `main/main` module and `main()` function). The entry of the execution is in `/app_name/main/main.py`, in the `main()` function.
* To execute the app you must write this command: `python -m app_name`

## Folders and Files

[Helpful doc](https://realpython.com/python-application-layouts/)

Folder:
* **config**: Archives for configuration and setup (yaml, json)
* **data**: DB seeds, CSV catalogs (only text) (used on deploy or initilization, not used for testing)
* **deploy**: Archives for deploying containers, CI pipelines, etc
* **docs**: any documentation for internal modules, handbooks, analysis and design documents, etc
* **scripts**: scripts that helps you in the development and maintenance process (NOT scripts for production use, those ones must be with the source code)
* **src**: source code of your application
* **src/app_name/package_hexagonal**: package to follow hexagonal+DDD+EDA architecture
* **tests**: contains every test of your app (unit, integration, functional and other tests)
* **tests/data**: raw data useful for testing (json, csv)

Files:
* **src/app_name/package_1/module_example.py**: example of how a good module should be
* **.editorconfig**: descripbe formating rules for you IDE o editor
* **.env.example**: copy/paste and rename to ".env" with correct values for good running
* **pyproject.toml**: file that helps build managers to pack this project (used to define dependencies, app data, etc). List of all the packages needed by your application. (better option than requirements.txt)
* **.pre-commit-config.yaml**: describe the checks to do before allowing new git commit


## Basic python project structure:

```bash
python-basic/
├── config
├── data
├── deploy
├── docs
├── scripts
├── src/app_name
│   ├── package_1
│   ├── package_2
│   ├── shared
├── tests
│   ├── data
│   ├── integration_tests
│   ├── unit_tests
│   │   ├── package_1
│   │   ├── package_2
│   │   ├── shared
├── .editorconfig
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── Makefile
├── pyproject.toml
└── README.md
```
