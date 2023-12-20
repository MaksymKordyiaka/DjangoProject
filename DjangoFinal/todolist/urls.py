from django.urls import path
from .views import task_list, add_task, edit_task, delete_task

urlpatterns = [
    path('', task_list, name='task_list'),
    path('add/', add_task, name='add_task'),
    path('edit/<int:id>/', edit_task, name='edit_task'),
    path('delete/<int:id>/', delete_task, name='delete_task'),
]