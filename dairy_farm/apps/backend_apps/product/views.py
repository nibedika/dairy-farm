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
from apps.backend_apps.company.models import Table as companyDB
from apps.backend_apps.product.models import Table as productDB


# Create your views here.
class Product():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg


	def add_product(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			# CATEGORY ::
			categoryWhere       = Q_set(status='active', trash=False)
			categoryInfo        = categoryDB.objects.filter(categoryWhere)

			# CATEGORY ::
			companyWhere       = Q_set(status='active', trash=False)
			companyInfo        = companyDB.objects.filter(companyWhere)

			if request.method == 'POST' and request.POST.get('product_add'):

				# CATEGORY ::
				sinCategoryWhere       = Q_set(category_id=request.POST.get('category_id'), status='active', trash=False)
				sinCategoryInfo        = categoryDB.objects.get(sinCategoryWhere)

				# CATEGORY ::
				sinCompanyWhere       = Q_set(company_id=request.POST.get('company_id'), status='active', trash=False)
				sinCompanyInfo        = companyDB.objects.get(sinCompanyWhere)

				# Data entry block start 
				data = productDB(
					product_id      = hp.unique_custom_id(hp, 'P'),
					category_id     = sinCategoryInfo,
					company_id      = sinCompanyInfo,
					name            = request.POST.get('name'),
					regular_price   = request.POST.get('regular_price'),
					current_price   = request.POST.get('current_price'),
					delivery_charge = request.POST.get('delivery_charge'),
					other_charge    = request.POST.get('other_charge'),
					image           = hp.file_processor(hp, request.FILES.get('product_img'), 'product', 'product/')
				)
				status = data.save()
				return redirect('all_product')
			
			elif request.method == 'GET':
				return render(request, 'product_add.html', {'menuData': menuInfo,'categoryData': categoryInfo,'companyData': companyInfo})

			return render(request, 'product_add.html', {'menuData': menuInfo,'categoryData': categoryInfo,'companyData': companyInfo})
		else:
			return redirect('home')



	def all_product(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)
			
			productWhere       = Q_set(status='active', trash=False)
			productInfo        = productDB.objects.filter(productWhere)

			return render(request, 'product_all.html', {'menuData': menuInfo, 'productData': productInfo})
		else:
			return redirect('home')



	def view_product(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			productWhere       = Q_set(id=id, status='active', trash=False)
			productInfo        = productDB.objects.get(productWhere)

			return render(request, 'product_view.html', {'menuData': menuInfo, 'productData': productInfo})
		else:
			return redirect('home')



	def edit_product(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			productWhere       = Q_set(id=id, status='active', trash=False)
			productInfo        = productDB.objects.get(productWhere)

			# CATEGORY ::
			categoryWhere       = Q_set(status='active', trash=False)
			categoryInfo        = categoryDB.objects.filter(categoryWhere)

			# CATEGORY ::
			companyWhere       = Q_set(status='active', trash=False)
			companyInfo        = companyDB.objects.filter(companyWhere)

			# Update Profile Picture And Cover Picture Start Here ------------->
			if request.method == 'POST' and request.POST.get('product_edit'):

				# CATEGORY ::
				sinCategoryWhere       = Q_set(category_id=request.POST.get('category_id'), status='active', trash=False)
				sinCategoryInfo        = categoryDB.objects.get(sinCategoryWhere)

				# CATEGORY ::
				sinCompanyWhere       = Q_set(company_id=request.POST.get('company_id'), status='active', trash=False)
				sinCompanyInfo        = companyDB.objects.get(sinCompanyWhere)

				if request.FILES.get('product_img') != None and request.FILES.get('product_img') != '':
					productFile = hp.file_processor(hp, request.FILES.get('product_img'), 'product', 'product/')
				else:
					productFile = productInfo.image

				# Data entry block start 
				where       = Q_set(id=id, status='active', trash=False)
				pre_update  = productDB.objects.select_related().filter(where)
				post_update = pre_update.update(
					category_id     = sinCategoryInfo,
					company_id      = sinCompanyInfo,
					name            = request.POST.get('name'),
					regular_price   = request.POST.get('regular_price'),
					current_price   = request.POST.get('current_price'),
					delivery_charge = request.POST.get('delivery_charge'),
					other_charge    = request.POST.get('other_charge'),
					status          = request.POST.get('status'),
					image           = productFile
			    )
				# Data entry block end
				return redirect('all_product') 
			
			elif request.method == 'GET':
				return render(request, 'product_edit.html', {'menuData': menuInfo, 'productData': productInfo,'categoryData': categoryInfo,'companyData': companyInfo})
			
			return render(request, 'product_edit.html', {'menuData': menuInfo, 'productData': productInfo,'categoryData': categoryInfo,'companyData': companyInfo})
		else:
			return redirect('home')



	def delete_product(request, id):
		if request.session.has_key('username'):

			productWhere       = Q_set(id=id, status='active', trash=False)
			productInfo        = productDB.objects.get(productWhere)

			productInfo.delete()
			return redirect('all_product')
		else:
			return redirect('home')