from django.urls import path
from apps.backend_apps.cost import views
 
urlpatterns = [
    path('add-cost/', views.Cost.add_cost, name='add_cost'),
    path('all-cost/', views.Cost.all_cost, name='all_cost'),
    path('edit-cost/<id>/', views.Cost.edit_cost, name='edit_cost'),
    path('delete-cost/<id>/', views.Cost.delete_cost, name='delete_cost'),
]