"""taskManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from task import views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home,name='home'),                                                           #主页
    url(r'^signup/$',accounts_views.signup,name='signup'),                                       #注册
    url(r'^login/$',auth_views.LoginView.as_view(template_name='login.html'),name='login'),      #登入
    url(r'^logout/$',auth_views.LogoutView.as_view(),name='logout'),                             #登出
    url(r'^add/$',views.add,name='add'),                                                         #增加任务
    url(r'^query/$',views.query,name='query'),                                                   #查询任务
    url(r'^delete/(?P<pk>\d+)/$', views.delete, name='delete'),                                  #删除任务
    url(r'^revise/(?P<pk>\d+)/$', views.revise, name='revise'),                                  #修改任务

    url(r'^reset/$',auth_views.PasswordResetView.as_view(                                        #密码重置
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
            ),name='password_reset'),

    url(r'^reset/done/$',auth_views.PasswordResetDoneView.as_view(                               #密码重置发起成功
    template_name='password_reset_done.html'),name='password_reset_done'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',  #密码重置确定
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),

    url(r'^reset/complete/$',                                                                    #密码重置完成
        auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'),
        name='password_reset_complete'),

    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(                          #修改密码
        template_name='password_change.html'),
        name='password_change'),

    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(                 #修改密码完成
        template_name='password_change_done.html'),
        name='password_change_done'),
]
