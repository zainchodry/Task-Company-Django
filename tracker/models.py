from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank = True)
    lead = models.ForeignKey(User, on_delete = models.CASCADE, related_name='lead_projects')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    



class Task(models.Model):
    project = models.ForeignKey(Project, on_delete = models.CASCADE, related_name="tasks")
    title = models.CharField(max_length = 200)
    description = models.TextField(blank = True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    due_date = models.DateField()
    completed = models.BooleanField(default = False)
    completed_at = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return self.title
    



class Report(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="reports")
    reporter = models.ForeignKey(User, on_delete = models.CASCADE, related_name="reports")
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Report by {self.reporter} on {self.date}"



