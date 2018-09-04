from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^grid$', views.grid, name='grid'),
    url(r'^layout$', views.layout, name='layout'),
    url(r'^text$', views.text, name='text'),
    url(r'^pic$', views.pic, name='pic'),
    url(r'^pic-text$', views.pic_text, name='pic-text'),
    url(r'^video$', views.video, name='video'),
    url(r'^input$', views.input, name='input'),
    url(r'^button$', views.button, name='button'),
    url(r'^section$', views.section, name='section'),
    url(r'^select$', views.select, name='select'),
    url(r'^$', views.page, name='page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
