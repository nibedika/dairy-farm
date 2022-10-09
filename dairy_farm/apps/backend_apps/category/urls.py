from django.urls import path
from apps.backend_apps.category import views
 
urlpatterns = [
    path('add-category/', views.Category.add_category, name='add_category'),
    path('all-category/', views.Category.all_category, name='all_category'),
    path('edit-category/<id>/', views.Category.edit_category, name='edit_category'),
    path('delete-category/<id>/', views.Category.delete_category, name='delete_category'),
]