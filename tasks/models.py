from django.db import models

# Create your models here.

class Task(models.Model):
    content = models.CharField(max_length=200)
    creator = models.TextField(null=True)