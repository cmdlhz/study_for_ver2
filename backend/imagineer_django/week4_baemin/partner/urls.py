from django.urls import path, re_path, include
from .views import index, signup

app_name = 'partner'

urlpatterns = [
  path('', index, name="index"),
  re_path(r'^signup/$', signup, name="signup")
]