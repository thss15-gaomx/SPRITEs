from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^layout/([0-9]*)$', views.layout, name='layout'),
    url(r'^text/([a-zA-Z0-9]*)$', views.text, name='text'),
    url(r'^pic/([a-zA-Z0-9]*)$', views.pic, name='pic'),
    url(r'^pic-text$', views.pic_text, name='pic-text'),
    url(r'^video$', views.video, name='video'),
    url(r'^input$', views.input, name='input'),
    url(r'^button$', views.button, name='button'),
    url(r'^section/([0-9]*)$', views.section, name='section'),
    url(r'^select/([a-zA-Z0-9]*)$', views.select, name='select'),
    url(r'^new-page$', views.new_page, name='new-page'),
    url(r'^delete/([a-zA-Z0-9]*)$', views.delete, name='delete'),
    url(r'^playbox$', views.playbox, name='playbox'),
    url(r'^$', views.page, name='page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
