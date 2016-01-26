from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^premises/', include('premises.urls')),
    url(r'^admin/', admin.site.urls),
]