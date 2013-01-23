from django.contrib import admin
from website.models import *
from django_ses.views import dashboard

admin.site.register_view('django-ses', dashboard, 'Django SES Stats')
admin.site.register(ContactForm)
admin.site.register(NewsletterSampleForm)
