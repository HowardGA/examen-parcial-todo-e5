from django import forms
from .models import Auditor, Application, Task

class AuditorForm(forms.ModelForm):
    class Meta:
        model = Auditor
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['app_name', 'description']
        widgets = {
            'app_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'description', 'status', 'due_date', 'auditor', 'application']
        widgets = {
            'task_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'auditor': forms.Select(attrs={'class': 'form-control'}),
            'application': forms.Select(attrs={'class': 'form-control'}),
        }