from django.urls import path
from . import views
from .views import group_list, create_group, join_group_by_name


urlpatterns = [
    path('', views.group_list, name='group_list'),
    path('create/', views.create_group, name='create_group'),
    path('community/group/join/<int:group_id>/', views.join_group_by_name, name='join_group_by_name'),
    path('group/<int:group_id>/', views.group_info, name='group_info'),
     path('group/<int:group_id>/chat/', views.group_chat, name='group_chat'),
    path('group/<int:group_id>/send_message/', views.send_message, name='send_message'),
    # path('join_success/<str:group_name>/', views.join_success, name='join_success'),
    path('joined_groups/', views.joined_groups, name='joined_groups'),
    
]
