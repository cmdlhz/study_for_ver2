from django.contrib import admin
from django.urls import include, path
from . import views
# For production, do not store static files in Django.
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.homepage),
  path('about/', views.about),
  path('articles/', include('articles.urls'))
]

urlpatterns += staticfiles_urlpatterns()