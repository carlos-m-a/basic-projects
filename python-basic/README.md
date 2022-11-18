# Python Basic Project Structure

## Keep in mind:

* Your new code must be under `src/python_basic/`. Create every new package there, and modify 'main' package code as well (but don't change the name of main package). The entry of the execution is in 'src/python_basic/main/main.py', in the `main()` function.
* Don't edit files in 'src' (that's it: `__init.py, __main__.py, runner.py`. Edit everything under `src/python_basic` (except 'main' package name)
* You should edit `python-basic` name (repository name) and `python_basic` (folder name in 'src') with your custom project name. (e.g.: `cars-manager` and `cars_manager`)


## Basic python project structure:

```bash
python-basic/
├── bin
│   └── some_script.py
├── data
│   └── input.csv
├── docs
│   └── handbook.md
├── src
│   ├── python_basic
│   │   ├── main
│   │   │   ├── __init__.py
│   │   │   ├── main.py
│   │   │   └── settings.py
│   │   ├── package_1
│   │   │   ├── __init__.py
│   │   │   ├── module_A.py
│   │   │   └── module_B.py
│   │   ├── package_2
│   │   │   ├── __init__.py
│   │   │   ├── module_C.py
│   │   │   └── module_D.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── __main__.py
│   └── runner.py
├── tests
│   ├── functional_tests
│   │   └── __init__.py
│   ├── integration_tests
│   │   ├── __init__.py
│   │   └── integration_test_1.py
│   ├── unit_tests
│   │   ├── package_1
│   │   │   ├── __init__.py
│   │   │   ├── module_A_tests.py
│   │   │   └── module_B_tests.py
│   │   ├── package_2
│   │   │   ├── __init__.py
│   │   │   ├── module_C_tests.py
│   │   │   └── module_D_tests.py
│   │   └── __init__.py
│   └── __init__.py
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py

```
