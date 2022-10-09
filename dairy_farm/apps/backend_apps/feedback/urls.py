from django.urls import path
from apps.backend_apps.feedback import views
 
urlpatterns = [
    path('add-feedback/', views.Feedback.add_feedback, name='add_feedback'),
    path('all-feedback/', views.Feedback.all_feedback, name='all_feedback'),
    path('view-feedback/<id>/', views.Feedback.view_feedback, name='view_feedback'),
    path('delete-feedback/<id>/', views.Feedback.delete_feedback, name='delete_feedback'),
]