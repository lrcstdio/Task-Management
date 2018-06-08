from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email=forms.CharField(max_length=254,required=True,widget=forms.EmailInput())#添加email字段
    class Meta:
        model = User  #指定表单模型为user
        fields = ('username','email','password1', 'password2')
