![Python](https://img.shields.io/badge/python-3.7.3-green.svg)
![Django](https://img.shields.io/badge/django-2.2.4-green.svg)
![Version](https://img.shields.io/badge/version-1.0.2-orange.svg)

# django-vb-admin

Creates custom Django project layout. Compatible with `Django 2.2.4` and
requires `Python 3.7.3` or higher version. By default, project uses **PostgreSQL**,
this means you need to install :) macOS users can install via `brew install postgres`

## Installation

```bash
$ createdb -E UTF8 -T template0 my_project_dev  # create your database
$ createdb -E UTF8 -T template0 --lc-collate=tr_TR.UTF-8 --lc-ctype=tr_TR.UTF-8 my_project_dev  # create your database with locale support
$ pip install django-vb-admin
```

## Usage

After installation, you’ll have a command: `django-vb-admin`

```bash
$ django-vb-admin -h

$ mkdir /path/to/my-django-project/
$ cd /path/to/my-django-project
$ django-vb-admin startproject                             # create structure to current working directory

# or
$ django-vb-admin startproject --target="/path/to/folder"  # create structure to given path
```

When creation completed, you can create your virtual environment and set your
environment variables:

```bash
export DJANGO_SECRET=$(head -c 75 /dev/random | base64 | tr -dc 'a-zA-Z0-9' | head -c 50)
export DATABASE_URL="postgres://localhost:5432/my_project_dev"
```

then;

```bash
$ pip install -r requirements/development.pip
```

Directory structure:

```bash
.
├── applications
├── config
│   ├── settings
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.example.py
│   │   ├── heroku.py
│   │   ├── production.py
│   │   └── test.example.py
│   ├── __init__.py
│   ├── urls.py
│   └── wsgi.py
├── requirements
│   ├── base.pip
│   ├── development.pip
│   ├── heroku.pip
│   └── production.pip
├── static
│   ├── css
│   │   └── application.css
│   ├── images
│   │   └── .gitkeep
│   └── js
│       └── .gitkeep
├── templates
│   └── custom_errors
│       ├── 400.html
│       ├── 403.html
│       ├── 404.html
│       └── 500.html
├── .bandit
├── .flake8
├── .isort.cfg
├── .pylintrc
├── .python-version
├── .ruby-version
├── .tm_properties
├── Procfile
├── manage.py
├── pyproject.toml
├── requirements.txt
└── runtime.txt
```

Now you can init `git`:

```bash
$ cd /path/to/my-django-project/
$ git init
```

## Packages

Common packages: `requirements/base.pip`

```bash
Django==2.2.4
django-vb-baseapp==1.0.0
Pillow==6.1.0
django-extensions==2.2.1
python-slugify==3.0.3
psycopg2-binary==2.8.3
dj-database-url==0.5.0
```

`django-vb-baseapp` makes the magic! Please check out at https://github.com/vbyazilim/django-vb-baseapp

Development packages: `requirements/development.pip`

```bash
-r base.pip
ipython==7.7.0
bpython==0.18
ptpython==2.0.4
Werkzeug==0.15.5
django-debug-toolbar==2.0
coverage==4.5.4
isort==4.3.21
black==19.3b0
flake8==3.7.8
flake8-bandit==2.1.1
flake8-blind-except==0.1.1
flake8-bugbear==19.3.0
flake8-builtins==1.4.1
flake8-polyfill==1.0.2
flake8-print==3.1.0
flake8-quotes==2.1.0
flake8-string-format==0.2.3
pylint==2.3.1
```

Heroku related packages: `requirements/heroku.pip`

```bash
-r base.pip
gunicorn==19.9.0
whitenoise==4.1.3
boto3==1.9.202
django-storages==1.7.1
```

Built-in support for **AWS-S3 Storage**. You need to create/get your:

- `S3_ACCESS_KEY_ID`
- `S3_SECRET_ACCESS_KEY`

and set those variables on Heroku. Please check `config/settings/heroku.py`
for more details. Basic Heroku setup:

```bash
$ heroku login
$ heroku apps:create
$ heroku addons:create heroku-postgresql:hobby-dev
$ heroku config:set DJANGO_ENV="heroku"
$ heroku config:set DJANGO_SECRET='YOUR_GENERATED_RANDOM_SECRET'
$ heroku config:set S3_ACCESS_KEY_ID='YOUR_S3_ACCESS_KEY_ID'
$ heroku config:set S3_SECRET_ACCESS_KEY='YOUR_S3_SECRET_ACCESS_KEY'
$ heroku config:set S3_BUCKET_NAME='YOUR_S3_BUCKET_NAME'
$ heroku config:set WEB_CONCURRENCY=3
$ git push heroku master
$ heroku run python manage.py migrate
$ heroku run python manage.py createsuperuser
```

If you want to use email reporter for Django errors, you need to set couple
more environment variables on Heroku side too.

Linux/Production packages: `requirements/production.pip`

```bash
-r base.pip
uWSGI==2.0.18
```

---

## License

This project is licensed under MIT

---

## Contributer(s)

* [Uğur "vigo" Özyılmazel](https://github.com/vigo) - Creator, maintainer

---

## Contribute

All PR’s are welcome!

1. `fork` (https://github.com/vbyazilim/django-vb-admin/fork)
1. Create your `branch` (`git checkout -b my-features`)
1. `commit` yours (`git commit -am 'added killer options'`)
1. `push` your `branch` (`git push origin my-features`)
1. Than create a new **Pull Request**!

---

## Change Log

**2019-08-07**

- Version bump: 1.0.2
- Add Rake tasks
- Fix MAFIFEST.in file
- Initial Beta relase: 1.0.0

---
