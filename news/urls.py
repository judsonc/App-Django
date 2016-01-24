# -*- coding: utf-8 -*-
from django.conf.urls import include, url, handler404
from . import views

urlpatterns = [
    #handler404 = 'views.page404'
    url(r'^$', views.home),
    url(r'^sobre/$', views.about),
    url(r'^contato/$', views.contact),
    url(r'^portfolio/$', views.portfolio),
    url(r'^servicos/$', views.services),
    url(r'^novidades/$', views.blog),
    url(r'^novidades/(?P<pk>[0-9]+)/$', views.post_detail),
]
