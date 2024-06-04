from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Auditor, Application, Task, OperationLog
from .forms import AuditorForm, ApplicationForm, TaskForm

def base(request):
    tasks = Task.objects.select_related('auditor', 'application').all()
    context = {'tasks': tasks}
    return render(request, 'base.html', context)


def delete_task(request, id_task):
    task = Task.objects.get(id_task=id_task)
    task.delete()
    return redirect('home')
from .forms import TaskForm

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tasks/')
    else:
        form = TaskForm()
        # Obtener los objetos de auditor y aplicación para pasar al formulario
        auditors = Auditor.objects.all()
        applications = Application.objects.all()
        # Pasar los objetos al formulario
        form.fields['auditor'].queryset = auditors
        form.fields['application'].queryset = applications
    return render(request, 'create_task.html', {'form': form})


# Vistas
def auditor_list(request):
    auditors = Auditor.objects.all()
    context = {'auditors': auditors}  # El nombre en el contexto debe ser 'auditors'
    return render(request, 'create_task.html', context)


def application_list(request):
    applications = Application.objects.all()  # Corregir el nombre de la variable
    context = {'applications': applications}  # El nombre en el contexto debe ser 'applications'
    return render(request, 'create_task.html', context)



def change_status(request, id_task, nuevo_estado):
    # Obtener la tarea específica
    task = Task.objects.get(id_task=id_task)
    
    # Verificar si el nuevo estado es válido
    if nuevo_estado in ['Pendiente', 'Progreso', 'Completado']:
        # Cambiar el estado de la tarea
        task.status = nuevo_estado
        task.save()
    
    # Redireccionar a la página de detalle de la tarea
    return redirect('detalle_tarea', task_id=id_task)
