from django.db import models
from django import forms

from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.core.validators import validate_image_file_extension
from django.core.validators import URLValidator

from apps.backend_apps.product.models import Table as productDB

# Create your models here.
class Table(models.Model):

	# General Info Fields
	date              = models.DateTimeField(auto_now_add=True)
	order_id          = models.CharField(max_length=50, blank=False)
	product_id        = models.ManyToManyField(productDB, related_name='ordered_product', blank=True)
	bill              = models.DecimalField(max_digits=99, decimal_places=3, blank=True)
	commission        = models.DecimalField(max_digits=99, decimal_places=3, blank=True)
	remission         = models.DecimalField(max_digits=99, decimal_places=3, blank=True)
	total             = models.DecimalField(max_digits=99, decimal_places=3, blank=True)
	
	# Customer Info
	customer_name     = models.CharField(max_length=250, blank=False)
	customer_contact  = models.CharField(max_length=250, blank=False)
	customer_address  = models.TextField(blank=True)
	customer_feedback = models.TextField(blank=True)
	customer_rating   = models.IntegerField(default=0, blank=True)
	
	status            = models.CharField(validators=[RegexValidator], max_length=50, default='active') #option-> active, poused, disabled 
	
	# Backup Fields
	trash             = models.BooleanField(default=False)
	
	def __str__(self):
		return self.order_id
