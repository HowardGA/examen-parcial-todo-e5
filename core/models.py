from django.db import models

class Auditor(models.Model):
    id_auditor = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'auditor'

    def __str__(self):
        return self.name

class Application(models.Model):
    id_application = models.AutoField(primary_key=True)
    app_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'application'

    def __str__(self):
        return self.app_name

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    id_task = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='pending')
    due_date = models.DateField(blank=True, null=True)
    auditor = models.ForeignKey(Auditor, on_delete=models.CASCADE, db_column='id_auditor')
    application = models.ForeignKey(Application, on_delete=models.CASCADE, db_column='id_application')

    class Meta:
        db_table = 'task'

    def __str__(self):
        return self.task_name

class OperationLog(models.Model):
    OPERATION_TYPE_CHOICES = [
        ('create', 'Create'),
        ('update', 'Update'),
        ('delete', 'Delete'),
    ]

    id_operationlog = models.AutoField(primary_key=True)
    operation_type = models.CharField(max_length=6, choices=OPERATION_TYPE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, db_column='task_id')
    auditor = models.ForeignKey(Auditor, on_delete=models.CASCADE, db_column='auditor_id')

    class Meta:
        db_table = 'operationlog'

    def __str__(self):
        return f"{self.operation_type} - {self.task.task_name}"