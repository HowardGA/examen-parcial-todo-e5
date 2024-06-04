from django.urls import path
from .views import (
    AuditorListView, AuditorCreateView, AuditorUpdateView, AuditorDeleteView,
    ApplicationListView, ApplicationCreateView, ApplicationUpdateView, ApplicationDeleteView,
    TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView
)

urlpatterns = [
    path('auditors/', AuditorListView.as_view(), name='home'),
    path('auditors/new/', AuditorCreateView.as_view(), name='auditor_new'),
    path('auditors/edit/<int:pk>/', AuditorUpdateView.as_view(), name='auditor_edit'),
    path('auditors/delete/<int:pk>/', AuditorDeleteView.as_view(), name='auditor_delete'),
    
    path('applications/', ApplicationListView.as_view(), name='application_list'),
    path('applications/new/', ApplicationCreateView.as_view(), name='application_new'),
    path('applications/edit/<int:pk>/', ApplicationUpdateView.as_view(), name='application_edit'),
    path('applications/delete/<int:pk>/', ApplicationDeleteView.as_view(), name='application_delete'),
    
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/new/', TaskCreateView.as_view(), name='task_new'),
    path('tasks/edit/<int:pk>/', TaskUpdateView.as_view(), name='task_edit'),
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
]