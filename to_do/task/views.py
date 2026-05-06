from django.shortcuts import render
from .models import AddTasks
from django.shortcuts import redirect, get_object_or_404
from .forms import Add_task, Update_task

def add_task(request):
    if request.method == 'POST':
        form = Add_task(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'temp/success.html')
        
    else:
        form = Add_task()

    return render(request, 'temp/index.html', {'form':form})

def update_task(request):
    if request.method == 'POST':
        form = Update_task(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'temp/success.html')
        
    else:
        form = Update_task()

    return render(request, 'temp/update.html', {'form':form})

def list_task(request):
    tasks = AddTasks.objects.all()
    return render(request, 'temp/list.html', {'tasks':tasks})

def delete_task(request,):
    task = get_object_or_404(AddTasks)
    task.delete()
    return redirect('list')