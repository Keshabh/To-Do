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

class Progress(models.Model):
    date=models.CharField(max_length=20)
    #it is to store the date every time user opens the app
    progress=models.IntegerField(default=0)
    total=models.IntegerField(default=0)
    #this contains how many work you have done in the specific date

class Chartcolor(models.Model):
    color=models.CharField(max_length=20,default="line")
    #stores the color for user to choose it for their graph and to change it permanently 

class Timer(models.Model):
    time=models.IntegerField(default=120)

class Audio(models.Model):
    audio_number = models.IntegerField(default=0)

class Audio_store(models.Model):
    record=models.FileField(upload_to='documents/')
    class Meta:
        db_table='Audio_store'

