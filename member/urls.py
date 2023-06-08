# @Project:     FundConnect
# @Filename:    urls.py
# @Author:      Daksh
# @Time:        08-06-2023 01:09 pm
from django.urls import path
from . import views

app_name = 'member'

urlpatterns = [
    path('', views.home, name='member-home'),
]