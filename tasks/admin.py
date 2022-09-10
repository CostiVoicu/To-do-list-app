from django.contrib import admin
from .models import task_model

# Register your models here.

class task_admin(admin.ModelAdmin):
    list_display = ['content', 'creator']

admin.site.register(task_model, task_admin)