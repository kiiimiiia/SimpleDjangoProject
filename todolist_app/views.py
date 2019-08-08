from django.shortcuts import render , redirect
from django.http import HttpResponse
from todolist_app.models import Tasklist
from todolist_app.forms import TaskForm
from django.contrib import messages

# Create your views here.
def todolist(request):

    if request.method == "POST" :
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,("New Task added!"))
        return redirect('todolist')

    else:
        all_tasks = Tasklist.objects.all
        return render(request , 'todolist.html', {'all_tasks' : all_tasks})


def contact(request):
    context ={
        'contact_text' : "Welcome contact page."
    }
    return render(request , 'contact.html', context)


def about(request):
    context ={
        'about_text' : "Welcome to About us page."
    }
    return render(request , 'about.html', context)