from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Auditor, Application, Task, OperationLog
from .forms import AuditorForm, ApplicationForm, TaskForm

# Vista para listar auditores
class AuditorListView(ListView):
    model = Auditor
    template_name = 'base.html'
    context_object_name = 'auditors'

# Vista para crear un auditor
class AuditorCreateView(CreateView):
    model = Auditor
    form_class = AuditorForm
    template_name = 'auditor_form.html'
    success_url = reverse_lazy('auditor_list')

# Vista para actualizar un auditor
class AuditorUpdateView(UpdateView):
    model = Auditor
    form_class = AuditorForm
    template_name = 'auditor_form.html'
    success_url = reverse_lazy('auditor_list')

# Vista para eliminar un auditor
class AuditorDeleteView(DeleteView):
    model = Auditor
    template_name = 'auditor_confirm_delete.html'
    success_url = reverse_lazy('auditor_list')

# Vista para listar aplicaciones
class ApplicationListView(ListView):
    model = Application
    template_name = 'application_list.html'
    context_object_name = 'applications'

# Vista para crear una aplicación
class ApplicationCreateView(CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'application_form.html'
    success_url = reverse_lazy('application_list')

# Vista para actualizar una aplicación
class ApplicationUpdateView(UpdateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'application_form.html'
    success_url = reverse_lazy('application_list')

# Vista para eliminar una aplicación
class ApplicationDeleteView(DeleteView):
    model = Application
    template_name = 'application_confirm_delete.html'
    success_url = reverse_lazy('application_list')

# Vista para listar tareas
class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

# Vista para crear una tarea
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')

# Vista para actualizar una tarea
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')

# Vista para eliminar una tarea
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task_list')