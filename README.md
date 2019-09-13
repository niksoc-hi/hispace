# hispace

hispace's django server

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Local Setup
- Install Postgres, look at .env/.local/.postgres for postgres settings
- Install python 3.6 and virtualenv
- Copy .env.template -> .env and set the environment variables
- Run the following commands:

      $ virtualenv -p python3.6 venv
      $ source venv/bin/activate
      $ pip install -r requirements/local.txt
      $ pre-commit install
      $ ./manage.py migrate
      $ ./manage.py runserver_plus

- To set up google login, create a new socialapp through /admin/socialaccount/socialapp/.
Fill in the form as follows:

    - Provider, “Google”
    - Name, your pick, suggest “Google”
    - Client id, is called “Client ID” by Google
    - Secret key, is called “Client secret” by Google
    - Key, is not needed, leave blank.

## Basic Commands

### Run server
    $ source venv/bin/activate
    $ ./manage.py runserver_plus

### Run pre-commit checks
We use pre-commit to install and manage git hooks. Some of the hooks include black (formatting) and code auditing (prospector).

    $ pre-commit run --all-files

### Test coverage

To run the tests, check your test coverage, and generate an HTML
coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

### Running tests with py.test

    $ pytest
