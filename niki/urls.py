from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
                       url(r'^api', views.apicall, name='apicall')
                       )
