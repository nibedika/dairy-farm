from django.urls import path
from apps.backend_apps.income import views
 
urlpatterns = [
    path('add-income/', views.Income.add_income, name='add_income'),
    path('all-income/', views.Income.all_income, name='all_income'),
    path('edit-income/<id>/', views.Income.edit_income, name='edit_income'),
    path('delete-income/<id>/', views.Income.delete_income, name='delete_income'),
]