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

class NewsletterSampleForm(models.Model):
	prefix = models.CharField(max_length=50)
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	suffix =  models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	streetaddress =  models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	state =  models.CharField(max_length=5)
	zipcode = models.CharField(max_length=5)
	industry = models.CharField(max_length=50)
	industryother = models.CharField(max_length=50)
	trendingquestions = models.BooleanField()
	sociallinks = models.BooleanField()
	products = models.BooleanField()
	custommessage = models.BooleanField()
	monthlygiveaway = models.BooleanField()
	color1 = models.CharField(max_length=7)
	color2 = models.CharField(max_length=7)
	color3 = models.CharField(max_length=7)
	color4 = models.CharField(max_length=7)

