from django.conf.urls import patterns, include, url
from website import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('website.views',
    # Examples:
    url(r'^$','index'),
	url(r'^pricing','pricing'),
	url(r'^sample','sample'),
	url(r'^signup','signup'),
	url(r'^about','about'),
	
	#Forms (Contact and Newsletter)
	url(r'^contact','contact'),
	url(r'^newslettersample','newslettersample'),
	
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf import settings

if settings.DEBUG:
	urlpatterns += patterns('',
		url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
	)