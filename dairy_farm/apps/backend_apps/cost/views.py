# Buildin Package
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q as Q_set
from package.helper import Helper as hp

# App's Model Import
from apps.access_apps.access.models import User as userDB
from apps.backend_apps.cost.models import Cl as costCL


# Create your views here.
class Cost():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def add_cost(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			# Add Start Here ------------->
			if request.method == 'POST' and request.POST.get('cost_add'):

				# Data entry block start 
				data = costCL(
					cost_id = hp.unique_custom_id(hp, 'EI'),
					user_id = menuInfo,
					field   = request.POST.get('field'),
					amount  = request.POST.get('amount'),
					remark  = request.POST.get('remark'),
				)
				status = data.save()
				return redirect('all_cost')
			
			elif request.method == 'GET':
				return render(request, 'cost_add.html', {'menuData': menuInfo})

			return render(request, 'cost_add.html', {'menuData': menuInfo})
		else:
			return redirect('home')



	def all_cost(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)
			
			costWhere = Q_set(trash=False)
			costInfo  = costCL.objects.filter(costWhere)

			return render(request, 'cost_all.html', {'menuData': menuInfo, 'costData': costInfo})
		else:
			return redirect('home')



	def edit_cost(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			costWhere = Q_set(id=id, status='active', trash=False)
			costInfo  = costCL.objects.get(costWhere)

			# Update Start Here ------------->
			if request.method == 'POST' and request.POST.get('cost_edit'):

				# Data entry block start 
				where       = Q_set(id=id, trash=False)
				pre_update  = costCL.objects.select_related().filter(where)
				post_update = pre_update.update(
					field          = request.POST.get('field'),
					amount         = request.POST.get('amount'),
					remark         = request.POST.get('remark'),
					status         = request.POST.get('status')
			    )
				# Data entry block end
				return redirect('all_cost') 

			elif request.method == 'GET':
				return render(request, 'cost_edit.html', {'menuData': menuInfo, 'costData': costInfo})
			
			return render(request, 'cost_edit.html', {'menuData': menuInfo, 'costData': costInfo})
		else:
			return redirect('home')



	def delete_cost(request, id):
		if request.session.has_key('username'):

			costWhere = Q_set(id=id, trash=False)
			costInfo  = costCL.objects.get(costWhere)

			costInfo.delete()
			return redirect('all_cost')
		else:
			return redirect('home')
