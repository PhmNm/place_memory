# PLace Memory App
[![py-img]][py-url]
[![django-img]][django-url]
![Static Badge](https://img.shields.io/badge/django--allauth-0.63.1-brightgreen)

## Key feature

- Login with Google (only save email and basic info of Google account).
- Add a new memory place by pointing the place on the map.
- Show saved memories and click on the place name to navigate on map.
- Click on the marker on the map to show the memory comments.

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

### Create OAuth 2.0 Client ID Credentials

- Access: [https://console.cloud.google.com](https://console.cloud.google.com)
- Create new project if not have yet
- Find or search for "Credentials" in APIs & Services
- Config "OAuth consent screen" with "External" option
- On screen Credentials click "CREATE CREDENTIALS" -> "OAuth client ID" to create OAuth 2.0 client id
  - Set Authorized redirect URIs as following:

```code
URIs 1:
http://127.0.0.1:8000/accounts/google/login/callback/
URIs 2:
http://127.0.0.1:8000/
```

- Save and use the generated ClientId & ClientSecret for setting in database.

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

### In case you don't want to use "Login with Google" feature

- Go into file: `myApp\templates\myApp\main.html`
- Change href value of "Login with Google" button into "accounts/login"
- Use the created superuser account to login the app

### Navigate to "localhost:8000/" to use app

[py-img]: https://img.shields.io/badge/_-3.9.19-yellow?logo=python&labelColor=white
[py-url]: https://docs.python.org/3.9/
[django-img]: https://img.shields.io/badge/_-4.2-brightgreen?logo=django&labelColor=black
[django-url]: https://docs.djangoproject.com/en/4.2/
