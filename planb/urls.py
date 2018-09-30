from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^layout/([0-9]*)$', views.layout, name='layout-b'),
    url(r'^text/([a-zA-Z0-9]*)$', views.text, name='text-b'),
    url(r'^select/([a-zA-Z0-9]*)$', views.select, name='select-b'),
    url(r'^section/([0-9]*)$', views.section, name='section-b'),
    url(r'^new-page$', views.new_page, name='new-page-b'),
    url(r'^delete/([a-zA-Z0-9]*)$', views.delete, name='delete-b'),
    url(r'^$', views.page, name='page-b'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
