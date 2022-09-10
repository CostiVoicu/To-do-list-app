from django.db import models

# Create your models here.

class task_model(models.Model):
    content = models.CharField(max_length=200)
    creator = models.CharField(max_length=50)