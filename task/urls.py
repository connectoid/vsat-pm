from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'task'

urlpatterns = [
    path('', views.index, name='index'),
    path('completed_tasks/', views.completed_tasks, name='completed_tasks'),
    path('task/', views.task_list, name='task_list'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('new_task/', views.task_create, name='new_task'),
    path('task/<int:task_id>/edit/', views.edit_task, name='edit_task'),
    path('new_work_type/', views.work_type_create, name='new_work_type'),
    path('new_client/', views.client_create, name='new_client'),
    path('new_customer/', views.customer_create, name='new_customer'),
    path('user_profile/<int:user_id>/', views.user_profile, name='user_profile'),
    path('client_profile/<int:client_id>/', views.client_profile, name='client_profile'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
]
