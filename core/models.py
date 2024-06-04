from django.db import models

# Within this table is the users that make the checkups to the mobile apps of the company
class Auditor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def _str_(self):
        return self.name
    
# This serves as a target to connect to the specific app
class Application(models.Model):
    app_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def _str_(self):
        return self.app_name

# This table grants tasks and connects them with the specific app
class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    task_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='pending')
    due_date = models.DateField(blank=True, null=True)
    auditor = models.ForeignKey(Auditor, on_delete=models.CASCADE)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)

    def _str_(self):
        return self.task_name

# Its basically a log that saves the specific operation that the audithors make while the checkuip
class OperationLog(models.Model):
    OPERATION_TYPE_CHOICES = [
        ('create', 'Create'),
        ('update', 'Update'),
        ('delete', 'Delete'),
    ]

    operation_type = models.CharField(max_length=6, choices=OPERATION_TYPE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    auditor = models.ForeignKey(Auditor, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.operation_type} - {self.task.task_name}"