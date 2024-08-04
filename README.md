# Kelp

## Overview

The goal is to make an easily-searchable database of seafood like that found in https://www.seafoodwatch.org/.


## Setup
1. Install [Poetry](https://python-poetry.org/docs/#installation) if you don't have it already.
2. Run `poetry install`
3. For all Django management commands, either prepend with `poetry run`, or run `poetry shell` and run all management commands within the poetry shell. [See more about the poetry shell](https://python-poetry.org/docs/basic-usage/#activating-the-virtual-environment)


## Development

`cd django_project` to use Django commands from within the project.

From `django_project`:
* `poetry run python manage.py runserver` to run the local dev server.
