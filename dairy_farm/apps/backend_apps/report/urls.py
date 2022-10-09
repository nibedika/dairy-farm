from django.urls import path
from apps.backend_apps.report import views
 
urlpatterns = [
    path('transaction-report/', views.Report.transaction_report, name='transaction_report'),
    path('revenue-report/', views.Report.revenue_report, name='revenue_report'),
    path('customer-report/', views.Report.customer_report, name='customer_report'),
]