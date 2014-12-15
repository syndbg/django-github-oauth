from django.conf.urls import patterns, url


urlpatterns = patterns('github_oath.views',
    url(r'^login/$', 'login', name='login'),
    url(r'^github-login/$', 'github_login'),
)
