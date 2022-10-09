# Buildin Package
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q as Q_set
from package.helper import Helper as hp

# App's Model Import
from apps.access_apps.access.models import User as userDB
from apps.backend_apps.company.models import Table as companyDB


# Create your views here.
class Company():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg


	def add_company(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			if request.method == 'POST' and request.POST.get('company_add'):

				# Data entry block start 
				data = companyDB(
					company_id = hp.unique_custom_id(hp, 'C'),
					name        = request.POST.get('name'),
				)
				status = data.save()
				return redirect('all_company')
			elif request.method == 'GET':
				return render(request, 'company_add.html', {'menuData': menuInfo})

			return render(request, 'company_add.html', {'menuData': menuInfo})
		else:
			return redirect('home')



	def all_company(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)
			
			companyWhere   = Q_set(status='active', trash=False)
			companyInfo    = companyDB.objects.filter(companyWhere)

			return render(request, 'company_all.html', {'menuData': menuInfo, 'companyData': companyInfo})
		else:
			return redirect('home')



	def edit_company(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)
			
			companyWhere   = Q_set(id=id, status='active', trash=False)
			companyInfo    = companyDB.objects.get(companyWhere)

			# Update Profile Picture And Cover Picture Start Here ------------->
			if request.method == 'POST' and request.POST.get('company_edit'):

				# Data entry block start 
				where       = Q_set(id=id, status='active', trash=False)
				pre_update  = companyDB.objects.select_related().filter(where)
				post_update = pre_update.update(
					name    = request.POST.get('name'),
					status  = request.POST.get('status'),
			    )
				# Data entry block end
				return redirect('all_company') 
			elif request.method == 'GET':
				return render(request, 'company_edit.html', {'menuData': menuInfo, 'companyData': companyInfo})
			return render(request, 'company_edit.html', {'menuData': menuInfo, 'companyData': companyInfo})
		else:
			return redirect('home')



	def delete_company(request, id):
		if request.session.has_key('username'):

			companyWhere       = Q_set(id=id, status='active', trash=False)
			companyInfo        = companyDB.objects.get(companyWhere)

			companyInfo.delete()
			return redirect('all_company')
		else:
			return redirect('home')