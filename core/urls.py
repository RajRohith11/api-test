from django.urls import path
from . import views

urlpatterns = [
    # Customer Endpoints
    path('customers/create/', views.create_customer, name='create_customer'),
    path('customers/', views.list_customers, name='list_customers'),

    # Account Endpoints
    path('accounts/create/', views.create_account, name='create_account'),
    path('accounts/<str:account_number>/', views.get_account_by_number, name='get_account_by_number'),
    path('accounts/<str:account_number>/update/', views.update_account, name='update_account'),
    path('accounts/<str:account_number>/delete/', views.delete_account, name='delete_account'),
    path('accounts/', views.get_all_accounts, name='get_all_accounts'),

    # Transaction Endpoints
    path('transactions/deposit/', views.deposit, name='deposit'),
    path('transactions/withdraw/', views.withdraw, name='withdraw'),
    path('transactions/transfer/', views.transfer, name='transfer'),
    path('transactions/<str:account_number>/', views.transaction_history, name='transaction_history'),
]
