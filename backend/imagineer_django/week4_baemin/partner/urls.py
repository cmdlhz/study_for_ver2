from django.urls import path, include
from .views import signup

app_name = 'partner'

urlpatterns = [
  path('', signup, name="signup")
]