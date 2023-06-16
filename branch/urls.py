# @Project:     FundConnect
# @Filename:    urls.py
# @Author:      Daksh
# @Time:        08-06-2023 01:09 pm
from django.urls import path
from . import views

app_name = 'branch'

urlpatterns = [
    path('', views.home, name='branch-home'),
    path('<int:pk>/', views.detail_branch, name='branch-detail-pk'),
    path('create/', views.create_branch, name='branch-create'),
    path('list/', views.list_branch, name='branch-list'),
    path('remittance/', views.remittance_form_view, name='branch-remittance'),
    path('edit/', views.edit_branch, name='branch-edit'),
    path('remove/', views.remove_branch, name='branch-remove'),
    path('<int:pk>/edit/', views.edit_selected_branch, name='branch-edit-pk'),

]
