from django.shortcuts import render, redirect
from tasks.models import task_model
from tasks.models import task_model

def home_view(request):
    tasks_list = task_model.objects.all()

    context = {
        'tasks': tasks_list,
    }

    return render(request, "home.html", context=context)

def delete_view(request, id):
    object = task_model.objects.get(id=id)
    if request.method == 'POST':
        object.delete()
        return redirect('/')
    context= {
        'task': object
    }
    return render(request, 'delete.html', context=context)