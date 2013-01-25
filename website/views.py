from django.shortcuts import render_to_response
from website.models import *
from django.template import RequestContext, Context, loader
from django.http import HttpResponse
from django.utils.html import escape
from django.shortcuts import render
from django.utils import simplejson
from django.core.mail import EmailMessage, EmailMultiAlternatives


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
		prefix = str(escape(request.POST['inputPrefix']))
		firstname = str(escape(request.POST['inputFirstName']))
		lastname = str(escape(request.POST['inputLastName']))
		suffix = str(escape(request.POST['inputSuffix']))
		email = str(escape(request.POST['inputEmail']))
		streetaddress = str(escape(request.POST['inputAddress']))
		city = str(escape(request.POST['inputCity']))
		state = str(escape(request.POST['inputState']))
		zipcode = str(escape(request.POST['inputZipcode']))
		industry = str(escape(request.POST['inputIndustry']))
		industryother = str(escape(request.POST['inputIndustryOther']))
		trendingquestions = str(escape(request.POST['inputTrendingQuestions']))
		sociallinks = str(escape(request.POST['inputSocialLinks']))
		products = str(escape(request.POST['inputProducts']))
		custommessage = str(escape(request.POST['inputCustomMessage']))
		monthlygiveaway = str(escape(request.POST['inputMonthlyGiveaway']))
		color1 = str(escape(request.POST['inputColor1']))
		color2 = str(escape(request.POST['inputColor2']))
		color3 = str(escape(request.POST['inputColor3']))
		color4 = str(escape(request.POST['inputColor4']))
		
		#Save object to database
		nsf= NewsletterSampleForm(prefix=prefix,firstname=firstname,lastname=lastname,suffix=suffix,email=email,streetaddress=streetaddress,
		city=city,state=state,zipcode=zipcode,industry=industry,trendingquestions=trendingquestions,sociallinks=sociallinks,products=products,
		monthlygiveaway = monthlygiveaway,color1=color1,color2=color2,color3=color3,color4=color4)
		nsf.save()
		try:
			name = prefix+" "+firstname+" "+lastname+" "+suffix
			address = streetaddress+" "+city+" "+state+" "+zipcode
			colors = color1+" "+color2+" "+color3+" "+color4
			trending = 'Trending Questions: '+trendingquestions
			social = 'Social Links: '+sociallinks
			product = 'Products: '+products
			custom = 'Custom Message: '+custommessage
			giveaway = "Monthly Giveaway: "+monthlygiveaway
			combine = name+"\n"+address+"\n"+colors+"\n"+trending+"\n"+social+"\n"+product+"\n"+giveaway+"\n"+custom
			sendtestemail(name,address,colors,trending,social,product,custom,giveaway)
			return HttpResponse("Object Saved and Email Sent");
		except:
			return HttpResponse("Message Saved. Email NOT sent due to ERROR");
	else:
		return HttpResponse("Email Failed");

#############################################
# Sends a sample email ######################
# Called from newsletter form submit#########
#############################################
def sendtestemail(name,address,colors,trending,social,product,custom,giveaway):
	from emailgenerator import *
	htmlemail = htmlemail('name','address','colors','trending','social','product','custom','giveaway')
	#Sends the emails
	subject, from_email, to = 'hello', SENDER, SENDER
	text_content = 'This is the default text fallback'
	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	msg.attach_alternative(htmlemail, "text/html")
	msg.send()
	
	
	
def test(request):
	from emailgenerator import *
	htmlemail = htmlemail('name','address','colors','trending','social','product','custom','giveaway')
	return HttpResponse(htmlemail)
	
	
	
	
	
	
	
	
	