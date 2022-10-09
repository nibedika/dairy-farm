# Buildin Package
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q as Q_set
from package.helper import Helper as hp

# App's Model Import
from apps.access_apps.access.models import User as userDB
from apps.backend_apps.income.models import Cl as incomeCL


# Create your views here.
class Income():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def add_income(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			# Add Start Here ------------->
			if request.method == 'POST' and request.POST.get('income_add'):

				# Data entry block start 
				data = incomeCL(
					income_id = hp.unique_custom_id(hp, 'EI'),
					user_id        = menuInfo,
					field          = request.POST.get('field'),
					amount         = request.POST.get('amount'),
					remark         = request.POST.get('remark'),
				)
				status = data.save()
				return redirect('all_income')
			
			elif request.method == 'GET':
				return render(request, 'income_add.html', {'menuData': menuInfo})

			return render(request, 'income_add.html', {'menuData': menuInfo})
		else:
			return redirect('home')



	def all_income(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)
			
			incomeWhere = Q_set(trash=False)
			incomeInfo  = incomeCL.objects.filter(incomeWhere)

			return render(request, 'income_all.html', {'menuData': menuInfo, 'incomeData': incomeInfo})
		else:
			return redirect('home')



	def edit_income(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			incomeWhere = Q_set(id=id, status='active', trash=False)
			incomeInfo  = incomeCL.objects.get(incomeWhere)

			# Update Start Here ------------->
			if request.method == 'POST' and request.POST.get('income_edit'):

				# Data entry block start 
				where       = Q_set(id=id, trash=False)
				pre_update  = incomeCL.objects.select_related().filter(where)
				post_update = pre_update.update(
					field          = request.POST.get('field'),
					amount         = request.POST.get('amount'),
					remark         = request.POST.get('remark'),
					status         = request.POST.get('status')
			    )
				# Data entry block end
				return redirect('all_income') 

			elif request.method == 'GET':
				return render(request, 'income_edit.html', {'menuData': menuInfo, 'incomeData': incomeInfo})
			
			return render(request, 'income_edit.html', {'menuData': menuInfo, 'incomeData': incomeInfo})
		else:
			return redirect('home')



	def delete_income(request, id):
		if request.session.has_key('username'):

			incomeWhere = Q_set(id=id, trash=False)
			incomeInfo  = incomeCL.objects.get(incomeWhere)

			incomeInfo.delete()
			return redirect('all_income')
		else:
			return redirect('home')
