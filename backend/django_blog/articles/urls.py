from django.urls import include, path
from . import views

urlpatterns = [
  path('', views.article_list),
  path('<slug>/', views.article_detail)
]