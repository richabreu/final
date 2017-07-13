#from django.conf.urls import patterns, url
from django.conf.urls import url
from django.contrib import admin
from final import views

#urlpatterns = patterns('', url(r'^$', views.index, name='index'))

urlpatterns = [
    url(r'^$', views.feeds, name='feeds'),
	#url(r'^feeds/$', views.feeds, name='feeds'),
    url(r'^tags/(?P<user_id>\w+)/$', views.tags, name='tags'),
]