# @Project:     FundConnect
# @Filename:    urls.py
# @Author:      Daksh
# @Time:        08-06-2023 01:09 pm
from django.urls import path
from . import views

app_name = 'member'

urlpatterns = [
    path('', views.home, name='member-home'),
    path('create/', views.create_member, name='member-create'),
    path('edit/', views.member_edit_search_view, name='member-edit'),
    path('<int:pk>/edit/', views.edit_selected_member, name='member-edit-pk'),
    path('remove/', views.remove_member, name='member-remove'),
    path('<int:pk>/remove/', views.remove_selected_member, name='member-remove-pk'),
    path('list/', views.view_member, name='member-view'),
    path('<int:pk>/view/', views.view_selected_member, name='member-view-pk'),
    path('ex-members/', views.terminated_members, name='member-terminated'),
]
