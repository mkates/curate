from django.template import loader, Context
from django.http import HttpResponse
#For context, a blank field will not render where as 
#any string will register as true

def htmlemail(RECEIVER,name,address,address2,trending,social,product,custom,giveaway,personal):
	template = loader.get_template('dentisttemplate.html')
	c = Context({"name": name,
		 "address": address,
		 "address2": address2,
		 "trending": parse(trending),
		 "social": parse(social),
		 "product":parse(product),
		 "custom": parse(custom),
		 "giveaway":parse(giveaway),
		 "personal":personal,
		})
	final_content_html = template.render(c)
	return final_content_html

def parse(booleanvalue):
	if booleanvalue == 'True':
		return 'True'
	else:
		return ''
		
def plainemail(RECEIVER,name,address,address2,trending,social,product,custom,giveaway,personal):
	template = loader.get_template('dentisttemplateplain.txt')
	c = Context({"name": name,
		 "address": address,
		 "address2": address2,
		 "trending": parse(trending),
		 "social": parse(social),
		 "product":parse(product),
		 "custom": parse(custom),
		 "giveaway":parse(giveaway),
		 "personal":personal,
		})
	final_content_plain = template.render(c)
	return final_content_plain