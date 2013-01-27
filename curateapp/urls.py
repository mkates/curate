from django.conf.urls import patterns, include, url
from website import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from adminplus import AdminSitePlus
admin.site = AdminSitePlus()
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$','website.views.index'),
    url(r'^test','website.views.test'),
	url(r'^pricing','website.views.pricing'),
	url(r'^sample','website.views.sample'),
	url(r'^signup','website.views.signup'),
	url(r'^about','website.views.about'),
	url(r'^privacy','website.views.privacy'),
	url(r'^terms','website.views.terms'),
	
	#Forms (Contact and Newsletter)
	url(r'^contact','website.views.contact'),
	url(r'^newslettersample','website.views.newslettersample'),
	
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    #Django Email Statistics
    url(r'^admin/django-ses/', include('django_ses.urls')),
)

from django.conf import settings

if settings.DEBUG:
	urlpatterns += patterns('',
		url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
	)