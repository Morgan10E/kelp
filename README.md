# Kelp

## Overview

The goal is to make an easily-searchable database of seafood like that found in https://www.seafoodwatch.org/.


## Setup
1. Install [Poetry](https://python-poetry.org/docs/#installation) if you don't have it already.
2. Run `poetry install`
3. For all Django management commands, either prepend with `poetry run`, or run `poetry shell` and run all management commands within the poetry shell. [See more about the poetry shell](https://python-poetry.org/docs/basic-usage/#activating-the-virtual-environment)


### Importing data

#### Import ratings

Use the custom command `add_ratings`, which takes a CSV file as input. For example, from the base directory:

```
poetry run python django_project/manage.py add_ratings test_data/ratings.csv
```


## Development

`cd django_project` to use Django commands from within the project.

From `django_project`:
* `poetry run python manage.py runserver` to run the local dev server.


## Testing

Test python with `pytest`.

Either

```
cd django_project
poetry run pytest
```

or

```
poetry run pytest django_project
```

When adding new tests, files should follow the convention `test_*.py` or edit the python_files match in `pyproject.toml`.
