from django.db import models
from django import forms
from django.forms import ModelForm

#################################
####### Contact Form ############
#################################
# Stores an object in the database as well as send as email to 
# the email in settings.py
class ContactForm(models.Model):
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	phone = models.CharField(max_length=20)
	industry = models.CharField(max_length=50)
