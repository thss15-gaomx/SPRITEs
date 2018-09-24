from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^swipe$', views.swipe, name='swipe'),
    url(r'^grid-b$', views.grid, name='grid-b'),
    url(r'^$', views.playbox, name='playbox'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
