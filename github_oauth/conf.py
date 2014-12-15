from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


class Config(object):

    def __init__(self, **kwargs):
        self.defaults = kwargs

    def __getattr_(self, name):
        try:
            return getattr(settings, name)
        except AttributeError:
            if name not in self.defaults:
                raise ImproperlyConfigured('[Django-Github-OAuth] Missing setting {0}'.format(name))


if __name__ != '__main__':
    conf = Config(
        CLIENT_ID=settings.GITHUB_CLIENT_ID,
        CLIENT_SECRET=settings.GITHUB_CLIENT_SECRET,
        REDIRECT_URI=settings.GITHUB_REDIRECT_URI,
        ACCEPT_TYPE='application/json',
    )
