![Python](https://img.shields.io/badge/python-3.7.4-green.svg)
![Django](https://img.shields.io/badge/django-2.2.6-green.svg)
![Version](https://img.shields.io/badge/version-1.0.9-orange.svg)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/638892d4f2bd4f04b2bc6c56881e8b99)](https://www.codacy.com/manual/vigo/django-vb-admin?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=vbyazilim/django-vb-admin&amp;utm_campaign=Badge_Grade)

# django-vb-admin

Creates custom Django project layout. Compatible with `Django 2.x` and
requires `Python 3.7.x` or higher version. By default, project uses **PostgreSQL**,
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
├── locale
│   └── tr
│       └── LC_MESSAGES
│           ├── django.mo
│           └── django.po
├── requirements
│   ├── base.pip
│   ├── development.pip
│   ├── heroku.pip
│   └── production.pip
├── static
│   ├── css
│   │   ├── application.css
│   │   └── bulma.min.0.7.5.css
│   ├── images
│   │   └── .gitkeep
│   └── js
│       ├── .gitkeep
│       ├── application.js
│       └── fontawesome.5.3.1.all.js
├── templates
│   ├── admin
│   │   └── base_site.html
│   ├── custom_errors
│   │   ├── 400.html
│   │   ├── 403.html
│   │   ├── 404.html
│   │   └── 500.html
│   └── base.html
├── .bandit
├── .flake8
├── .gitignore
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
django-vb-baseapp==1.0.1
Django==2.2.6
Pillow==6.2.0
django-extensions==2.2.3
python-slugify==3.0.6
psycopg2-binary==2.8.3
dj-database-url==0.5.0
```

`django-vb-baseapp` makes the magic! Please check out at https://github.com/vbyazilim/django-vb-baseapp

Development packages: `requirements/development.pip`

```bash
-r base.pip
ipython==7.8.0
bpython==0.18
ptpython==2.0.6
Werkzeug==0.16.0
django-debug-toolbar==2.0
coverage==4.5.4
isort==4.3.21
black==19.3b0
flake8==3.7.8
flake8-bandit==2.1.2
flake8-blind-except==0.1.1
flake8-bugbear==19.8.0
flake8-builtins==1.4.1
flake8-polyfill==1.0.2
flake8-print==3.1.1
flake8-quotes==2.1.0
flake8-string-format==0.2.3
pylint==2.4.2
```

Heroku related packages: `requirements/heroku.pip`

```bash
-r base.pip
gunicorn==19.9.0
whitenoise==4.1.4
boto3==1.9.253
django-storages==1.7.2
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

**2019-10-20**

- Upgrade python packages

**2019-09-19**

- Add Codacy integration
- Add setup completed message

**2019-08-12**

- Add `templates/base.html` using [Bulma.io][bulma] 0.7.5
- Add `templates/admin/` for base admin site.
- Add `static/js/application.js`
- Add global locale path
- Version bump: 1.0.4
- Version bump: 1.0.5 (*Fix README file*)


**2019-08-07**

- Add `--version` option, version bump to 1.0.3
- Version bump: 1.0.2
- Add Rake tasks
- Fix MAFIFEST.in file
- Initial Beta relase: 1.0.0

---

[bulma]: https://bulma.io
