from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description']

class QueryForm(forms.Form):
    key=forms.CharField(max_length=10)
