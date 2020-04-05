from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from . import views
from textanalysis.views import gettext


urlpatterns = [
    path('', views.gettext, name = 'gettext'), 
] 