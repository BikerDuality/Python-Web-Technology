from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404
import datetime,random
from .models import Product

def homepage(request):
	template=loader.get_template('index.html')
	quotes=['xxxxxxxx','yyyyyyyyyyyy']
	html=template.render({'quote':random.choice(quotes)}).encode()
	return HttpResponse(html)

def about(request):
	template=loader.get_template('about.html')
	html=template.render().encode()
	return HttpResponse(html)

def show_list(request,order='sku',filter=''):
	products=Product.objects.order_by(order).filter(name__contains=filter)
	template=loader.get_template('list.html')
	html=template.render(locals()).encode()
	return HttpResponse(html)

def detail(request,sku):
	product=get_object_or_404(Product,sku=sku)
	template=loader.get_template('detail.html')
	html=template.render(locals()).encode()
	return HttpResponse(html)

