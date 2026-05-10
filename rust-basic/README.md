# Rust Basic Project Structure

## Description

Template repo for rust language projects


## Folders and Files

Folder:
* **config**: Archives for configuration and setup (yaml, json)
* **data**: DB seeds, CSV catalogs (only text) (used on deploy or initilization, not used for testing)
* **deploy**: Archives for deploying containers, CI pipelines, etc
* **docs**: any documentation for internal modules, handbooks, analysis and design documents, etc
* **scripts**: scripts that helps you in the development and maintenance process (NOT scripts for production use, those ones must be with the source code)
* **src**: source code of your application
* **src/package_hexagonal**: package to follow hexagonal+DDD+EDA architecture
* **tests**: contains every test of your app (unit, integration, functional and other tests)
* **tests/data**: raw data useful for testing (json, csv)

Files:
* **.editorconfig**: descripbe formating rules for you IDE o editor
* **.env.example**: copy/paste and rename to ".env" with correct values for good running
* **.pre-commit-config.yaml**: describe the checks to do before allowing new git commit


## Basic project structure:

```bash
generic-basic/
├── config
├── data
├── deploy
├── docs
├── scripts
├── src
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
├── Cargo.toml
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── Makefile
└── README.md
```
