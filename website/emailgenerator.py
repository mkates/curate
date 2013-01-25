from django.template import loader, Context
from django.http import HttpResponse
#For context, a blank field will not render where as 
#any string will register as true

def htmlemail(name,address,colors,trending,social,product,custom,giveaway):
	template = loader.get_template('dentisttemplate.html')
	c = Context({"name": 'Dr. Alan Stern, DMD',
		 "address": '34 Pavers Way',
		 "address2": 'Waltham, NJ 07723',
		 "trending":trending,
		 "social":social,
		 "product":product,
		 "custom":custom,
		 "giveaway":giveaway,
		})
	final_content_html = template.render(c)
	return final_content_html