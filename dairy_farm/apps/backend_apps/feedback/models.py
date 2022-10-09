from django.db import models
from django import forms

from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.core.validators import validate_image_file_extension
from django.core.validators import URLValidator

from apps.backend_apps.product.models import Table as productDB


# Create your models here.
class Cl(models.Model):

	# General Info Fields
	date        = models.DateTimeField(auto_now_add=True)
	feedback_id = models.CharField(max_length=50, blank=False)
	
	name        = models.CharField(max_length=255, blank=True)
	contact     = models.CharField(max_length=55, blank=True)
	email       = models.CharField(max_length=155, blank=True)
	product     = models.ForeignKey(productDB, on_delete=models.CASCADE, related_name='feedback_product', blank=True)
	description = models.TextField(blank=True)
	rating      = models.CharField(max_length=15, blank=True)
	
	status      = models.CharField(validators=[RegexValidator], max_length=50, default='unseen') #option-> seen, unseen 
	
	# Backup Fields
	trash       = models.BooleanField(default=False)
	
	def __str__(self):
		return self.feedback_id
