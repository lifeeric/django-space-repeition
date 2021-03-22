# install

```sh
poetry init
poetry add django
poetry run django-admin startproject config .
poetry shell # activate shell
poetry export -f requirements.txt > requirements.txt

poetry install # use the lock file to install the dependencies
```