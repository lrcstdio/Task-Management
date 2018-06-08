from django import forms
from .models import Task

class TaskForm(forms.ModelForm):            #任务表单，这里只有description字段
    class Meta:
        model = Task
        fields = ['description']

class QueryForm(forms.Form):                #查询表单，key查询关键字
    key=forms.CharField(max_length=10)
