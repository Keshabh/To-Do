from django.db import models
from django.db.models.fields import TextField
from django.contrib.auth.models import User,auth

# Create your models here

class Tasks(models.Model):
    tasks=models.CharField(max_length=200)
    #done: 1 means done, 0 means not done
    done=models.IntegerField(default=0)
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    

class Recurring(models.Model):
    tasks=models.CharField(max_length=200)
    #done: 1 means done, 0 means not done
    done=models.IntegerField(default=0)
    #add another field data to store date, so we can refresh recurring task everyday.
    date=models.IntegerField(default=0)
    userid = models.ForeignKey(User,on_delete=models.CASCADE)

class Progress(models.Model):
    date=models.CharField(max_length=20)
    #it is to store the date every time user opens the app
    progress=models.IntegerField(default=0)
    total=models.IntegerField(default=0)
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    #this contains how many work you have done in the specific date

class Chartcolor(models.Model):
    color=models.CharField(max_length=20,default="line")
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    #stores the color for user to choose it for their graph and to change it permanently 

class Timer(models.Model):
    time=models.IntegerField(default=120)
    userid = models.ForeignKey(User,on_delete=models.CASCADE)

class Audio(models.Model):
    audio_number = models.IntegerField(default=0)
    userid = models.ForeignKey(User,on_delete=models.CASCADE)

class Audio_store(models.Model):
    record=models.FileField(upload_to='documents/')
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        db_table='Audio_store'
    
