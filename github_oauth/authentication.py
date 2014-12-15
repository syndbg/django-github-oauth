import requests

from django.contrib.auth import get_user_model

from conf import conf
from links import ACCESS_TOKEN_URL, PROFILE_DATA_URL

User = get_user_model()


class GithubOAuthentication(object):

    def authenticate(self, code):
        payload = {'code': code, 'client_id': conf.CLIENT_ID, 'client_secret': conf.CLIENT_SECRET,
                   'redirect_uri': conf.REDIRECT_URI}
        headers = {'Accept': conf.ACCEPT_TYPE}
        response = requests.post(ACCESS_TOKEN_URL, params=payload, headers=headers)
        json = response.json()
        access_token = json['access_token']
        try:
            return User.objects.get(token=access_token)
        except User.DoesNotExist:
            user_info = self.get_user_info(access_token)
            return User.objects.create(**user_info)

    def get_user_info(self, token):
        response = requests.post(PROFILE_DATA_URL.format(token=token))
        json = response.json()
        username = json['login']
        password = User.objects.make_random_password(length=10)
        return {username: username, password: password, token: token}

    def get_user(self, token):
        try:
            return User.objects.get(token=token)
        except User.DoesNotExist:
            return
