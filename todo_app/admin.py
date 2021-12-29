from django.contrib import admin
from .models import Tasks,Recurring,Progress,Chartcolor,Timer
# Register your models here.
admin.site.register(Tasks)
admin.site.register(Recurring)
admin.site.register(Progress)
admin.site.register(Chartcolor)
admin.site.register(Timer)
