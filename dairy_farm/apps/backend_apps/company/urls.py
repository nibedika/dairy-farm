from django.urls import path
from apps.backend_apps.company import views
 
urlpatterns = [
    path('add-company/', views.Company.add_company, name='add_company'),
    path('all-company/', views.Company.all_company, name='all_company'),
    path('edit-company/<id>/', views.Company.edit_company, name='edit_company'),
    path('delete-company/<id>/', views.Company.delete_company, name='delete_company'),
]