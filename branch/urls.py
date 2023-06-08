# @Project:     FundConnect
# @Filename:    urls.py
# @Author:      Daksh
# @Time:        08-06-2023 01:09 pm
from django.urls import path
from . import views

app_name = 'branch'

urlpatterns = [
    path('', views.home, name='branch-home'),
    path('create/', views.create_branch, name='branch-create'),
    path('list/', views.list_branch, name='branch-list'),
]
