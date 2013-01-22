from django.shortcuts import render_to_response
from website.models import *
from django.template import RequestContext
from django.http import HttpResponse
from django.utils.html import escape
from django.shortcuts import render
from django.utils import simplejson
from django.core.mail import send_mail


#############################################
# Main Website Page Rendering ###############
#############################################

def index(request):
	return render_to_response('index.html',context_instance=RequestContext(request))

def sample(request):
	return render_to_response('sample.html',context_instance=RequestContext(request))
	
def pricing(request):
	return render_to_response('pricing.html',context_instance=RequestContext(request))
	
def signup(request):
	return render_to_response('signup.html',context_instance=RequestContext(request))

def about(request):
	return render_to_response('about.html',context_instance=RequestContext(request))


#############################################
# Sign up Contact Form ######################
#############################################
def contact(request):
	if request.method == 'POST':
		#Escape sanitizes the data
		name1 = str(escape(request.POST['inputName']))
		phone1 = str(escape(request.POST['inputPhone']))
		email1 = str(escape(request.POST['inputEmail']))
		industry1 = str(escape(request.POST['inputIndustry']))
		cf = ContactForm(name=name1,email=email1,phone=phone1,industry=industry1)
		cf.save()
		####CREATE NEW EMAIL ADDRESS AND PASSWORD TO ENABLE FUNCTIONALITY
		try:
			contents = name1 +"\n"+email1 +"\n"+phone1+"\n"+industry1
			send_mail("Curate Inquiry", contents, email1,['mhkates@gmail.com'], fail_silently=False)
			return HttpResponse("success");
		except:
			return HttpResponse("testsuccess");
	else:
		return HttpResponse("failed");

#############################################
# Newsletter Sample Form ####################
#############################################
def contact(request):
	if request.method == 'POST':
		#Escape sanitizes the data
		name1 = str(escape(request.POST['inputName']))
		phone1 = str(escape(request.POST['inputPhone']))
		email1 = str(escape(request.POST['inputEmail']))
		industry1 = str(escape(request.POST['inputIndustry']))
		cf = ContactForm(name=name1,email=email1,phone=phone1,industry=industry1)
		cf.save()
		####CREATE NEW EMAIL ADDRESS AND PASSWORD TO ENABLE FUNCTIONALITY
		try:
			contents = name1 +"\n"+email1 +"\n"+phone1+"\n"+industry1
			send_mail("Curate Inquiry", contents, email1,['mhkates@gmail.com'], fail_silently=False)
			return HttpResponse("success");
		except:
			return HttpResponse("testsuccess");
	else:
		return HttpResponse("failed");
