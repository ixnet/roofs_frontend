from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from . import views


app_name = 'roof'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^roofs$', views.list, name='list'),
    url(r'^(?P<slug>[\w-]+)/$', views.detail, name='detail'),

]
