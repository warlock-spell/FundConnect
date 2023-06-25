# @Project:     FundConnect
# @Filename:    urls.py
# @Author:      Daksh Gaur
# @Email:       hi@daksh.fyi
# @Time:        24-06-2023 03:40 pm
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='cashbook-home'),
    path('create/', views.create_cashbook_entry, name='cashbook-create'),
    path('search/', views.search_cashbook, name='cashbook-search'),
    path('<int:pk>/<str:financial_year>/cashbook/', views.view_cashbook, name='cashbook-view'),
    path('transactions/', views.search_transactions, name='transactions-search'),
    path('<str:year>/<str:month>/<str:date>/transactions/', views.transaction_by_date, name='transactions-view'),
    path('all/', views.view_all_cashbook, name='cashbook-all'),
    path('branch/', views.create_branch_entry, name='branch-cashbook-create'),
    path('branch/<int:date>/<int:month>/<int:year>/', views.list_branch_for_entry, name='cashbook-branches-list'),
    path('branch/<int:pk>/<int:date>/<int:month>/<int:year>/', views.create_entry_for_selected_branch,
         name='cashbook-entry-selected-branch'),
    path('apply-for-loan/', views.loan_application, name='loan-apply'),
]
