from django.urls import path
from django.conf.urls import include, url
from .views import upload_artwork, success, images
from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from . import views


urlpatterns = [
    path('', views.upload_artwork, name = 'upload_artwork'), 
    path('success', views.success, name = 'success'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)