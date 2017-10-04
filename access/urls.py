from django.conf.urls import url, include
from .views import index, signup, invalid, logout, log_in, auth_check, home


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'signup/$', signup, name='signup'),
    url(r'^invalid/$', invalid, name="invalid"),
    url(r'^logout/$',logout, name='logout'),
    url(r'^log_in/$', log_in, name='log_in'),
    url(r'^auth_check/$', auth_check, name='check'),
    url(r'^home/$', home, name='home'),

]
