from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from django.http import HttpResponse
from .models import Task
from django.contrib.auth.models import User
from .forms import TaskForm,QueryForm
def home(request):
    return render(request,'home.html')

def add(request):
    if request.method =='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.create_by=request.user
            task.save()
            return redirect('home')
    else:
        form=TaskForm()
    return render(request,'add.html',{'form':form})

def delete(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return redirect('home')

def revise(request,pk):
    oldtask=Task.objects.get(id=pk)
    if request.method =='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            oldtask.description=request.POST['description']
            oldtask.save()
            return redirect('home')
    else:
        form=TaskForm()
    return render(request,'revise.html',{'form':form,'oldtask':oldtask})

def query(request):
    if request.method=='POST':
        form=QueryForm(request.POST)
        if form.is_valid():
            key=request.POST['key']
            tasks=Task.objects.filter(create_by=request.user).filter(description__contains=key)
            return render(request,'query_result.html',{'tasks':tasks})
    else:
        form=QueryForm()
    return render(request,'query.html',{'form':form})
