# Buildin Package
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q as Q_set
from package.helper import Helper as hp

# App's Model Import
from apps.access_apps.access.models import User as userDB
from apps.backend_apps.contact.models import Cl as contactCL


# Create your views here.
class Contact():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def add_contact(request):

		# COMMON INFO FETCHING START
		if request.session.has_key('web_username'):
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			userInfo        = userDB.objects.get(userWhere)
		else:
			userInfo        = ''

		menuWhere           = Q_set(designation='admin', status="active", trash=False)
		menuInfo            = userDB.objects.filter(menuWhere).last()
		# COMMON INFO FETCHING END

		# Add Start Here ------------->
		if request.method == 'POST' and request.POST.get('contact_add'):

			# Data entry block start 
			data = contactCL(
				contact_id  = hp.unique_custom_id(hp, 'FCI'),
				name        = request.POST.get('name'),
				contact     = request.POST.get('contact'),
				email       = request.POST.get('email'),
				subject     = request.POST.get('subject'),
				description = request.POST.get('description')
			)
			status = data.save()
			return redirect('add_contact')
		
		elif request.method == 'GET':
			return render(request, 'contact_add.html', {'active': 'contact', 'menuData': menuInfo, 'userData': userInfo})

		return render(request, 'contact_add.html', {'active': 'contact', 'menuData': menuInfo, 'userData': userInfo})



	def all_contact(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)
			
			contactWhere = Q_set(trash=False)
			contactInfo  = contactCL.objects.filter(contactWhere)

			return render(request, 'contact_all.html', {'menuData': menuInfo, 'msgData': msgInfo, 'contactData': contactInfo})
		else:
			return redirect('home')



	def view_contact(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			contactWhere = Q_set(id=id, trash=False)
			contactInfo  = contactCL.objects.get(contactWhere)

			return render(request, 'contact_view.html', {'menuData': menuInfo, 'msgData': msgInfo, 'contactData': contactInfo})
		else:
			return redirect('home')



	def delete_contact(request, id):
		if request.session.has_key('username'):

			contactWhere = Q_set(id=id, trash=False)
			contactInfo  = contactCL.objects.get(contactWhere)

			contactInfo.delete()
			return redirect('all_contact')
		else:
			return redirect('home')
