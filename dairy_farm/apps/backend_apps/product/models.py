from django.db import models
from django import forms

from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.core.validators import validate_image_file_extension
from django.core.validators import URLValidator

from apps.backend_apps.category.models import Table as categoryTable
from apps.backend_apps.company.models import Table as companyTable


# Create your models here.
class Table(models.Model):

	# General Info Fields
	date            = models.DateTimeField(auto_now_add=True)
	product_id      = models.CharField(max_length=50, blank=False)
	
	category_id     = models.ForeignKey(categoryTable, on_delete=models.CASCADE, related_name='product_category_id')
	company_id      = models.ForeignKey(companyTable, on_delete=models.CASCADE, related_name='product_company_id')
	
	name            = models.CharField(max_length=50, blank=False)
	regular_price   = models.DecimalField(max_digits=99, decimal_places=3, blank=True)
	current_price   = models.DecimalField(max_digits=99, decimal_places=3, blank=True)
	delivery_charge = models.DecimalField(max_digits=99, decimal_places=3, blank=True)
	other_charge    = models.DecimalField(max_digits=99, decimal_places=3, blank=True)
	image           = models.FileField(max_length=100, blank=True)
	
	status          = models.CharField(validators=[RegexValidator], max_length=50, default='active') #option-> active, inactive 
	
	# Backup Fields
	trash           = models.BooleanField(default=False)
	
	def __str__(self):
		return self.product_id
