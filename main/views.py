﻿from django.shortcuts import render

from django.http import Http404
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from .models import Category, Order, Mail
import requests

def mainpage(request):
	#initialize variables
	args={}
	args.update(csrf(request))

	

	args['categories'] = Category.objects.all()
	return render_to_response('main/main.htm',args)

def contacts(request):
	#initialize variables
	args={}
	args.update(csrf(request))

	

	args['categories'] = Category.objects.all()
	return render_to_response('main/contacts.html',args)

def send_message(request):
	#init variables
	args={}
	args.update(csrf(request))
	if request.POST:
		name = request.POST['name']
		email = request.POST['email']
		message = request.POST['message']

		mail = Mail.objects.create(name=name, email=email, body=message)
		mail.save()
		args['success_message'] = "Ваше сообщение успешно отправлено."
		return render_to_response('main/main.htm',args)
	else:
		return redirect(reverse('main:contacts'))

def add_order(request):
	message = "mydodo:"
	args={}
	args.update(csrf(request))

	args['categories'] = Category.objects.all()
	if request.POST:
		name = request.POST['name']
		category = request.POST['category']
		date = request.POST['date']
		time = request.POST['time']
		address = request.POST['address']
		telephone = request.POST['telephone']
		date = date + " " + time
		if request.POST['yes'] == 'kvartira':
			rooms = request.POST['rooms']
			order = Order.objects.create(name=name, telephone=telephone,category=category, date_of_order=date , address=address, value=rooms)
			order.save()
		else:
			area = request.POST['ofis']
			order = Order.objects.create(name=name, telephone=telephone,category=category, date_of_order=date , address=address, value=area)
			order.save()

		args['success_message'] = "Ваша заявка принята."
		message += '\ndate:' + str(date.encode('utf-8')) + '\n telephone:' + str(telephone.encode('utf-8'))
		sms_url = 'http://smsc.ru/sys/send.php?login=shimanazar&psw=shima1318&phones=996557081318&mes='
		sms_url += message
		r = requests.get(sms_url)
		return render_to_response('main/main.htm',args)
	else:
		return render_to_response('main/order_form.html',args)







