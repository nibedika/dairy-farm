# Buildin Package
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q as Q_set
from package.helper import Helper as hp

# App's Model Import
from apps.access_apps.access.models import User as userDB
from apps.backend_apps.category.models import Table as categoryDB


# Create your views here.
class Category():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg


	def add_category(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			if request.method == 'POST' and request.POST.get('category_add'):

				# Data entry block start 
				data = categoryDB(
					category_id = hp.unique_custom_id(hp, 'C'),
					name        = request.POST.get('name'),
				)
				status = data.save()
				return redirect('all_category')
			elif request.method == 'GET':
				return render(request, 'category_add.html', {'menuData': menuInfo})

			return render(request, 'category_add.html', {'menuData': menuInfo})
		else:
			return redirect('home')



	def all_category(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)
			
			categoryWhere   = Q_set(status='active', trash=False)
			categoryInfo    = categoryDB.objects.filter(categoryWhere)

			return render(request, 'category_all.html', {'menuData': menuInfo, 'categoryData': categoryInfo})
		else:
			return redirect('home')



	def edit_category(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)
			
			categoryWhere   = Q_set(id=id, status='active', trash=False)
			categoryInfo    = categoryDB.objects.get(categoryWhere)

			# Update Profile Picture And Cover Picture Start Here ------------->
			if request.method == 'POST' and request.POST.get('category_edit'):

				# Data entry block start 
				where       = Q_set(id=id, status='active', trash=False)
				pre_update  = categoryDB.objects.select_related().filter(where)
				post_update = pre_update.update(
					name    = request.POST.get('name'),
					status  = request.POST.get('status'),
			    )
				# Data entry block end
				return redirect('all_category') 
			elif request.method == 'GET':
				return render(request, 'category_edit.html', {'menuData': menuInfo, 'categoryData': categoryInfo})
			return render(request, 'category_edit.html', {'menuData': menuInfo, 'categoryData': categoryInfo})
		else:
			return redirect('home')



	def delete_category(request, id):
		if request.session.has_key('username'):

			categoryWhere       = Q_set(id=id, status='active', trash=False)
			categoryInfo        = categoryDB.objects.get(categoryWhere)

			categoryInfo.delete()
			return redirect('all_category')
		else:
			return redirect('home')