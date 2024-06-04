from django.urls import path
from .views import (
    base, create_task, delete_task, change_status, auditor_tasks, TaskUpdateView
)

urlpatterns = [
    path('tasks/', base, name='home'),
    path('tasks/delete/<int:id_task>/', delete_task, name='delete_task'),
    path('tasks/new/', create_task, name='create_task'),
    path('tasks/auditor/<int:auditor_id>/', auditor_tasks, name='auditor_tasks'),
    path('tasks/edit/<int:pk>/', TaskUpdateView.as_view(), name='edit_task'),
]
