from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^grid$', views.grid, name='grid'),
    url(r'^settings$', views.settings, name='settings'),
    url(r'^text$', views.text, name='text'),
    url(r'^$', views.select, name='select'),
]
