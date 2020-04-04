from django.urls import path
from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.post_detail, name='post_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)