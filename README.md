# PLace Memory App
[![py-img]][py-url]
[![django-img]][django-url]
![Static Badge](https://img.shields.io/badge/django--allauth-0.63.1-brightgreen)

## Environment & dependencies

- Pythyon: 3.9.19
- Django: 4.2
- django-allauth: 0.63.1
- Database: default db.sqlite3

## Installation guide

Make sure to use the right version of python for most compatible

### Clone the project

```terminal
git clone https://github.com/PhmNm/place_memory.git
```

### Install dependencies

```terminal
pip install -r requirements.txt
```

## Setup project

### Create superuser

```terminal
python manage.py createsuperuser
```

### Migrate model to schema

```terminal
python manage.py migrate
```

### Setup social application in admin site

- Create localhost site in Site model
- Create an application in Social application model as below information
  - Provider: Google
  - Provider id: google
  - Name: Google or any name you want
  - Client id & Secret key: your Google app OAuth 2.0 Client information or contact for my key
  - Sites: above localhost site created in Site model

### Navigate to "localhost:8000/" to use app

[py-img]: https://img.shields.io/badge/_-3.9.19-yellow?logo=python&labelColor=white
[py-url]: https://docs.python.org/3.9/
[django-img]: https://img.shields.io/badge/_-4.2-brightgreen?logo=django&labelColor=black
[django-url]: https://docs.djangoproject.com/en/4.2/
