from django.db import models
from django.db.models.fields import TextField

# Create your models here

class Tasks(models.Model):
    tasks=models.CharField(max_length=200)
    #done: 1 means done, 0 means not done
    done=models.IntegerField(default=0)

class Recurring(models.Model):
    tasks=models.CharField(max_length=200)
    #done: 1 means done, 0 means not done
    done=models.IntegerField(default=0)
    #add another field data to store date, so we can refresh recurring task everyday.
    date=models.IntegerField(default=0)
