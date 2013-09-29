from django.conf.urls import patterns, url

from larb import views

urlpatterns = patterns('',
     url(r'^$', views.index, name='index')
)