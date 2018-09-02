from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^grid$', views.grid, name='grid'),
    url(r'^layout$', views.layout, name='layout'),
    url(r'^text$', views.text, name='text'),
    url(r'^pic$', views.pic, name='pic'),
    url(r'^$', views.select, name='select'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
