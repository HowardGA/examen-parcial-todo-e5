from django.urls import path
from .views import (
    base,create_task,delete_task,change_status
)

urlpatterns = [
    path('auditors/', base, name='home'),
    path('auditors/delete/<int:id_task>/',delete_task, name='delete_task'),
    path('auditors/new/', create_task, name='create_task'),
    ##path('auditors/<int:id_task>/<str:nuevo_estado>/', change_status, name='change_status'),
]