# Create custom and tailor made Django project!

Creates custom Django project layout. Compatible with `Django 2.2.8` and
requires `Python 3.7.x`. By default, project uses **PostgreSQL**,
this means you need to install :) macOS users can install via `brew install postgres`

## Requirements

- Python 3.7.x
- PostgreSQL

## Installation

```bash
$ pip install django-vb-admin
```

This package heavily depends on [django-vb-baseapp](https://github.com/vbyazilim/django-vb-baseapp).
All the rake tasks are related to `django-vb-baseapp`. You don’t need to do
anything, `django-vb-admin` installs required packages automatically.

## Usage

After installation, you’ll have a command: `django-vb-admin`

```bash
$ django-vb-admin -h

usage: django-vb-admin [-h] [-t TARGET] [-v {0,1}] [--version]
                       [{startproject}]

Create new Django project

positional arguments:
  {startproject}        Name of command(s)

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Target path
  -v {0,1}, --verbosity {0,1}
                        Verbose mode
  --version             show program's version number and exit
```

Now you can check the [example page](https://vbyazilim.github.io/django-vb-admin/example/)

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
1. `commit` yours (`git commit -am 'Add awesome feature'`)
1. `push` your `branch` (`git push origin my-features`)
1. Than create a new **Pull Request**!
