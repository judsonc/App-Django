# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^sobre/$', views.about),
    url(r'^contato/$', views.contact),
    url(r'^novidades/$', views.blog),
    url(r'^novidades/(?P<pk>[0-9]+)/$', views.post_detail),
]
