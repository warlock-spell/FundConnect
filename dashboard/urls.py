# @Project:     FundConnect
# @Filename:    urls.py
# @Author:      Daksh
# @Time:        08-06-2023 01:08 pm
from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('edit/', views.edit_dashboard, name='dashboard-edit'),
    path('', views.view_dashboard, name='dashboard-home'),
]
