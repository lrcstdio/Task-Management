from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Task(models.Model):
    description=models.CharField(max_length=30)
    create_by=models.ForeignKey(User,related_name='tasks')

    def __str__(self):
        return self.description
