# Buildin Package
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q as Q_set
from package.helper import Helper as hp

# App's Model Import
from apps.access_apps.access.models import User as userDB
from apps.backend_apps.order.models import Table as orderDB


# Create your views here.
class Report():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg


	def transaction_report(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)
			
			orderWhere       = Q_set(status='active', trash=False)
			orderInfo        = orderDB.objects.filter(orderWhere)

			return render(request, 'transaction_report.html', {'menuData': menuInfo, 'orderData': orderInfo})
		else:
			return redirect('home')



	def revenue_report(request):
		if request.session.has_key('username'):
			from django.db.models import Sum

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)
			
			orderWhere       = Q_set(status='active', trash=False)
			orderInfo        = orderDB.objects.filter(orderWhere)

			return render(request, 'revenue_report.html', {'menuData': menuInfo, 'orderData': orderInfo})
		else:
			return redirect('home')



	def customer_report(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)
			
			orderWhere       = Q_set(status='active', trash=False)
			orderInfo        = orderDB.objects.filter(orderWhere)

			return render(request, 'customer_report.html', {'menuData': menuInfo, 'orderData': orderInfo})
		else:
			return redirect('home')
