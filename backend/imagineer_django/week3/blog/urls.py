from django.contrib import admin
from django.urls import include, path, re_path
from . import views

app_name = 'blog'

urlpatterns = [
  path('', views.index, name='index'),
  re_path(r'^(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
  # path('about/', views.about, name='about'),
]