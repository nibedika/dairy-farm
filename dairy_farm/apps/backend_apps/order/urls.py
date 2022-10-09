from django.urls import path
from apps.backend_apps.order import views
 
urlpatterns = [
    path('add-order/', views.Order.add_order, name='add_order'),
    path('all-order/', views.Order.all_order, name='all_order'),
    path('view-order/<id>/', views.Order.view_order, name='view_order'),
    path('edit-order/<id>/', views.Order.edit_order, name='edit_order'),
    path('delete-order/<id>/', views.Order.delete_order, name='delete_order'),
]