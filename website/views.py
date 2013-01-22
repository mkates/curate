from django.shortcuts import render_to_response
from website.models import *
from django.template import RequestContext
from django.http import HttpResponse
from django.utils.html import escape
from django.utils import simplejson
from django.shortcuts import render

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
	