from django.conf.urls import url, include
from . import views


urlpatterns = [
    #url(r'^music/(?P<albumId>[0-9]+)/', views.index, name='index'),
    url(r'^$', views.index, name='index'),
]

