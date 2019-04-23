from django.contrib import admin
from django.urls import include, re_path
from . import views
# For production, do not store static files in Django.
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
  re_path(r'^admin/', admin.site.urls),
  re_path(r'^$', views.homepage),
  re_path(r'^about/$', views.about),
  re_path(r'^articles/', include('articles.urls'))
]

urlpatterns += staticfiles_urlpatterns()