from django.conf.urls import patterns, include, url

from blog import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^post/(?P<p_id>\d+)/$', views.detail, name='detail'),
        url(r'^tag/(?P<t_id>\w+)/$', views.tag, name='tag'),
        )
