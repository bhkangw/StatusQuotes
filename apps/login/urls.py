from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^main', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^users/(?P<id>\d+)$', views.show),
    url(r'^logout$', views.logout),
    url(r'^$', views.redirects),
    # url(r'^dashboard$', views.dashboard),
]
