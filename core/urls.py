# @Project:     FundConnect
# @Filename:    urls.py
# @Author:      Daksh
# @Time:        08-06-2023 12:38 pm

from django.urls import path

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
]