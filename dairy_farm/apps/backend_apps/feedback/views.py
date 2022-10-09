# Buildin Package
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q as Q_set
from package.helper import Helper as hp

# App's Model Import
from apps.access_apps.access.models import User as userDB
from apps.backend_apps.feedback.models import Cl as feedbackCL
from apps.backend_apps.product.models import Table as productDB


# Create your views here.
class Feedback():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def add_feedback(request):

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

		productWhere        = Q_set(status='active', trash=False)
		productInfo         = productDB.objects.filter(productWhere)

		# Add Start Here ------------->
		if request.method == 'POST' and request.POST.get('feedback_add'):

			pWhere        = Q_set(id=request.POST.get('product'), status='active', trash=False)
			pInfo         = productDB.objects.get(pWhere)

			# Data entry block start 
			data = feedbackCL(
				feedback_id = hp.unique_custom_id(hp, 'FI'),
				name        = request.POST.get('name'),
				contact     = request.POST.get('contact'),
				email       = request.POST.get('email'),
				product     = pInfo,
				description = request.POST.get('description'),
				rating      = request.POST.get('rating')
			)
			status = data.save()
			return redirect('add_feedback')
		
		elif request.method == 'GET':
			return render(request, 'feedback_add.html', {'active': 'feedback', 'menuData': menuInfo, 'userData': userInfo, 'productData': productInfo})

		return render(request, 'feedback_add.html', {'active': 'feedback', 'menuData': menuInfo, 'userData': userInfo, 'productData': productInfo})



	def all_feedback(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = feedbackCL.objects.filter(msgWhere)
			
			feedbackWhere = Q_set(trash=False)
			feedbackInfo  = feedbackCL.objects.filter(feedbackWhere)

			return render(request, 'feedback_all.html', {'menuData': menuInfo, 'msgData': msgInfo, 'feedbackData': feedbackInfo})
		else:
			return redirect('home')



	def view_feedback(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = feedbackCL.objects.filter(msgWhere)

			feedbackWhere = Q_set(id=id, trash=False)
			feedbackInfo  = feedbackCL.objects.get(feedbackWhere)

			return render(request, 'feedback_view.html', {'menuData': menuInfo, 'msgData': msgInfo, 'feedbackData': feedbackInfo})
		else:
			return redirect('home')



	def delete_feedback(request, id):
		if request.session.has_key('username'):

			feedbackWhere = Q_set(id=id, trash=False)
			feedbackInfo  = feedbackCL.objects.get(feedbackWhere)

			feedbackInfo.delete()
			return redirect('all_feedback')
		else:
			return redirect('home')
