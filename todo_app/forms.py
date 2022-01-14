from django import forms
from django.db import models
from django.db.models import fields
from .models import *
class Add_Task(forms.ModelForm):
    class Meta:
        model= Tasks
        fields= ['tasks']

class R_Add_Task(forms.ModelForm):
    class Meta:
        model= Recurring
        fields= ['tasks']


class AudioForm(forms.ModelForm):
    class Meta:
        model=Audio_store
        fields=['record']

