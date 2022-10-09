from django.urls import path
from apps.backend_apps.product import views
 
urlpatterns = [
    path('add-product/', views.Product.add_product, name='add_product'),
    path('all-product/', views.Product.all_product, name='all_product'),
    path('view-product/<id>/', views.Product.view_product, name='view_product'),
    path('edit-product/<id>/', views.Product.edit_product, name='edit_product'),
    path('delete-product/<id>/', views.Product.delete_product, name='delete_product'),
]