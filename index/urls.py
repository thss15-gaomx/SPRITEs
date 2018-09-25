from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^help5$', views.help5, name='help5'),
    url(r'^help4$', views.help4, name='help4'),
    url(r'^help3$', views.help3, name='help3'),
    url(r'^help2$', views.help2, name='help2'),
    url(r'^help1$', views.help1, name='help1'),
    url(r'^$', views.index, name='index'),
]
