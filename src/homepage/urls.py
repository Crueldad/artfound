from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.post_detail, name='post_detail'),
]