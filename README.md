# Django Github OAuth


A backend to authenticate users in a Django web app using Github's OAuth.


![Unicorn](http://i.imgur.com/lvAH97u.png)


# Installation

via setuptools

```
python setup.py install
```

via PyPi

```
pip install django-github-oauth
```


# Usage


1. Add `github_oauth` in your `project/settings.py`'s INSTALLED apps.


```
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'github_oauth',
)
```

2. Add `github_oauth.authentication.GithubOAuthentication` to your auth backends.


```
AUTHENTICATION_BACKENDS = (
    'github_oauth.authentication.GithubOAuthentication',
)
```


3. Create a Github OAuth application. You can do so [here](https://github.com/settings/applications/new)

4. In your `project/settings.py` set the following variables from the newly created Github OAuth app:

* GITHUB_CLIENT_ID
* GITHUB_CLIENT_SECRET
* GITHUB_REDIRECT_URI

Copy-paste very carefully. :sweat_smile:
