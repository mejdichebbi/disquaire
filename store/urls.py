from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    url(r'^$', views.listing),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail),
]