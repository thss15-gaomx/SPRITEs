from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.grid, name='grid-b'),
    url(r'^text$', views.text, name='text-b'),
    url(r'^pic$', views.pic, name='pic-b'),
    url(r'^select$', views.select, name='select-b'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
