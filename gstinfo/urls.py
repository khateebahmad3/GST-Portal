from django.conf.urls import url

from . import views

app_name = 'gstinfo'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^test/$', views.testit, name='testit'),
	url(r'^login/$', views.log_in, name='log_in'),
	url(r'^logout/$', views.log_out, name='log_out'),
	url(r'^user-dashboard/$', views.success, name='user-dashboard'),
	url(r'^user/registrations/$', views.registrations, name='registrations'),
	url(r'^user/(?P<operation>.+)/addnew/$', views.addform, name='addform'),
	url(r'^user/returns/$', views.returns, name='returns'),
	url(r'^user/registrations/(?P<value>.+)/edit/$', views.updateregform, name='updateregform'),
	url(r'^user/returns/(?P<month>.+)/(?P<value>.+)/edit/$', views.updateretform, name='updateretform'),
	url(r'^user/sessionexpired/$', views.sessionexpire, name='sessionexpire'),
	url(r'^getclients/$', views.getClients, name='getClients'),
	url(r'^getreturns/$', views.getReturns, name='getReturns'),
]