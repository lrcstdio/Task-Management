from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from django.http import HttpResponse
from .models import Task
from django.contrib.auth.models import User
from .forms import TaskForm,QueryForm
def home(request):           #主页
    return render(request,'home.html')

def add(request):            #增加任务
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

def delete(request,pk):    #删除任务
    task=Task.objects.get(id=pk)
    task.delete()
    return redirect('home')

def revise(request,pk):    #修改任务
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

def query(request):       #查询任务
    if request.method=='POST':
        form=QueryForm(request.POST)
        if form.is_valid():
            key=request.POST['key']
            tasks=Task.objects.filter(create_by=request.user).filter(description__contains=key)     #筛选属于当前用户且包含关键字的任务
            return render(request,'query_result.html',{'tasks':tasks})
    else:
        form=QueryForm()
    return render(request,'query.html',{'form':form})
