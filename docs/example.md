# Example

We’re going to create a Django project skeleton!

## Let’s create project:

```bash
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
│   │   └── bulma.min.X.X.X.css
│   ├── images
│   │   └── .gitkeep
│   └── js
│       ├── .gitkeep
│       ├── application.js
│       └── fontawesome.X.X.X.all.js
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

## Shipped Packages

Common packages: `requirements/base.pip`

```bash
Django==2.2.8
Pillow==6.2.1
django-extensions==2.2.5
python-slugify==4.0.0
psycopg2-binary==2.8.4
dj-database-url==0.5.0
django-vb-baseapp
vb-console
```

Development packages: `requirements/development.pip`

```bash
-r base.pip
ipython==7.10.0
ipdb==0.12.3
prompt-toolkit==2.0.10
bpython==0.18
ptpython==2.0.6
Werkzeug==0.16.0
django-debug-toolbar==2.1
coverage==4.5.4
isort==4.3.21
black==19.10b0
flake8==3.7.9
flake8-bandit==2.1.2
flake8-blind-except==0.1.1
flake8-bugbear==19.8.0
flake8-builtins==1.4.1
flake8-polyfill==1.0.2
flake8-print==3.1.4
flake8-quotes==2.1.1
flake8-string-format==0.2.3
pylint==2.4.4
```

**Note**: Package order is important here. Due to `prompt-toolkit` dependency
on `ipdb` and `ptpython`, we need to install specific version: `prompt-toolkit==2.0.10`
in the given order. Packages are test on Python 3.8.0 environment and had
issues with `ipdb`, `ipython` and other repls.

Heroku related packages: `requirements/heroku.pip`

```bash
-r base.pip
gunicorn==20.0.4
whitenoise==4.1.4
boto3==1.10.33
django-storages==1.8
```

Linux/Production packages: `requirements/production.pip`

```bash
-r base.pip
uWSGI==2.0.18
```

## Heroku and AWS

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
