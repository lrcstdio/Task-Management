from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib.auth import login as auth_login
# Create your views here.
def signup(request):                    #定义注册视图
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():             #如果表单有效
            user=form.save()            #保存并写入数据库
            auth_login(request,user)    #登入用户
            return redirect('home')     #重定向网页为主页
    else:
        form=SignUpForm()               #如果请求为GET则传入一个表单
    return render(request,'signup.html',{'form':form})
