from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.http import HttpResponse

from .models import ToDo

from .forms import ToDoForm


def home(request):

    todos = ToDo.objects.all().order_by('-created_at')

    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = ToDoForm()

    return render(request, 'todo/home.html',{'todos':todos, 'form': form})


def update_todo(request, pk):

    todo = get_object_or_404(ToDo, pk=pk)

    if request.method == 'POST':
        form  = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ToDoForm(instance=todo)

    return render(request, 'todo/update_todo.html', {'form': form, 'todo': todo})

def delete_todo(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    todo.delete()
    return redirect('home')

def toggle_todo(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect('home')
