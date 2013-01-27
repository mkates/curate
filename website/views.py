from django.shortcuts import render_to_response
from website.models import *
from django.template import RequestContext, Context, loader
from django.http import HttpResponse
from django.utils.html import escape
from django.shortcuts import render
from django.utils import simplejson
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.utils.encoding import smart_str
from emailgenerator import *

#Universal variables
SENDER = 'curateioinfo@gmail.com'

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

def privacy(request):
	return render_to_response('privacy.html',context_instance=RequestContext(request))

def terms(request):
	return render_to_response('terms.html',context_instance=RequestContext(request))

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
			#message = EmailMessage("Curate Inquiry", contents, SENDER,['curateioinfo@gmail.com'])
			#message.send()
			print "Email Success"
			return HttpResponse("success");
		except:
			print "Email Failed"
			return HttpResponse("testsuccess");
	else:
		return HttpResponse("failed");

#############################################
# Newsletter Sample Form ####################
#############################################
def newslettersample(request):
	if request.method == 'POST':
		#Escape sanitizes the data
		prefix = smart_str(escape(request.POST['inputPrefix']))
		firstname = smart_str(escape(request.POST['inputFirstName']))
		lastname = smart_str(escape(request.POST['inputLastName']))
		suffix = smart_str(escape(request.POST['inputSuffix']))
		email = smart_str(escape(request.POST['inputEmail']))
		streetaddress = smart_str(escape(request.POST['inputAddress']))
		city = smart_str(escape(request.POST['inputCity']))
		state = smart_str(escape(request.POST['inputState']))
		zipcode = smart_str(escape(request.POST['inputZipcode']))
		industry = smart_str(escape(request.POST['inputIndustry']))
		industryother = smart_str(escape(request.POST['inputIndustryOther']))
		personalmessage = smart_str(escape(request.POST['inputPersonalMessage']))
		trendingquestions = 'False'
		if ('inputTrendingQuestions' in request.POST):
			trendingquestions = 'True'
		sociallinks = 'False'
		if ('inputSocialLinks' in request.POST):
			sociallinks = 'True'
		products = 'False'
		if ('inputProducts' in request.POST):
			products = 'True'
		custommessage = 'False'
		if ('inputCustomMessage' in request.POST):
			custommessage = 'True'
		monthlygiveaway = 'False'
		if ('inputMonthlyGiveaway' in request.POST):
			monthlygiveaway = 'True'
		
		#Save object to database
		nsf= NewsletterSampleForm(prefix=prefix,firstname=firstname,lastname=lastname,suffix=suffix,email=email,streetaddress=streetaddress,
		city=city,state=state,zipcode=zipcode,industry=industry,trendingquestions=trendingquestions,sociallinks=sociallinks,products=products,
		monthlygiveaway = monthlygiveaway,personalmessage=personalmessage)
		nsf.save()
		name = prefix+" "+firstname+" "+lastname+" "+suffix
		address = streetaddress
		address2 = city+" "+state+", "+zipcode
		trending = trendingquestions
		social = sociallinks
		product = products
		custom = custommessage
		giveaway = monthlygiveaway
		personal = personalmessage
		emailresponse = sendtestemail(email,name,address,address2,trending,social,product,custom,giveaway,personal)
		return HttpResponse(emailresponse);
	else:
		return HttpResponse("Email Failed");


#############################################
# Sends a sample email ######################
# Called from newsletter form submit#########
#############################################
def sendtestemail(RECEIVER,name,address,address2,trending,social,product,custom,giveaway,personal):
	html_email = htmlemail(RECEIVER,name,address,address2,trending,social,product,custom,giveaway,personal)
	#Sends the emails
	try:
		subject, from_email, to = 'hello', SENDER, RECEIVER 
		text_content = 'This is the default text fallback'
		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		msg.attach_alternative(html_email, "text/html")
		msg.send()
		return "Success"
	except:
		return "Error connecting email"
	
	
def test(request):
	html_email = htmlemail('test@test.com','Mitch Kates','1 main street','brockton mA','True','True','True','False','False','A personal message')
	return HttpResponse(html_email)
	
	
	
	
	
	
	
	
	