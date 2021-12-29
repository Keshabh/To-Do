from django.http.response import HttpResponsePermanentRedirect,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from datetime import date
import calendar
from .forms import Add_Task,R_Add_Task
from django.contrib.auth.models import User,auth


from todo_app.models import Chartcolor, Progress, Tasks,Recurring, Timer
# Create your views here.
curr_date = date.today()
day=calendar.day_name[curr_date.weekday()]
tme=datetime.datetime.today().strftime('%d/%m/%Y')
date=day + "\n" + tme
h=0
dates = datetime.datetime.now()
'''date = dates.strftime("%c").split(' ')
date=date[0]+'- '+ date[2]+' '+date[1]+','+date[4][2:]

date = str(dates)
print("Date: ",date)
'''
def index(request):    
    h=0
    '''
    if request.method == 'POST':
        fm=Add_Task(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Add_Task()
    elif request.method=='GET':
        fm=Add_Task()'''
    T=Tasks.objects.all()
    #calculate total tasks done today from Tasks and Recurring
    #delete todays task data from Progress
    #add new data with todays date and progress value stored in p
    p=len(Recurring.objects.filter(done=1)) + len(Tasks.objects.filter(done=1))
    try:
     d = Progress.objects.filter(date=tme)
     d.delete()
    except:
        pass
    #update progress
    obj = Progress(date=tme,progress=p)
    obj.save()
     


    return render(request,'index.html',{'time':date,'T':T,'H':h})

def add(request):
    if request.method=='GET':
        if not request.user.is_authenticated:
            return redirect('account/login')
        h=1
        fm=Add_Task()  
    else:
        h=0
        fm=Add_Task(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Add_Task() 
    T=Tasks.objects.all()
    return render(request,'index.html',{'time':date,'T':T,'form':fm,'H':h})

def delete(request,id):
    if request.method=='POST':
        d = Tasks.objects.get(pk=id)
        d.delete()
        return HttpResponseRedirect('/')
  

def update(request,id):
    if request.method=='POST':
        h=1
        u = Tasks.objects.get(pk=id)
        upd= Add_Task(request.POST,instance=u)
        if upd.is_valid():
            upd.save()
            return HttpResponseRedirect('/')
    else:
        h=0
        u = Tasks.objects.get(pk=id)
        upd= Add_Task(instance=u)
    T=Tasks.objects.all()
    tiu=Tasks.objects.get(pk=id)
    return render(request,'update.html',{'time':date,'T':T,'form':upd,'H':h,'ti':tiu})

def finished(request,id):
    if request.method=='GET':
        #if done=1, set it to 0
        #ELSE, set it to 1
        #Tasks.objects.filter(pk=id).update(done = 1)
        T=Tasks.objects.get(pk=id)
        if T.done==0:
            Tasks.objects.filter(pk=id).update(done = 1)
        else:
            Tasks.objects.filter(pk=id).update(done = 0)
        return HttpResponseRedirect('/')

def delete_all(request):
    if request.method=='GET':
        T=Tasks.objects.all()
        T.delete()
        return HttpResponseRedirect('/')

def clear_finished(request):
    if request.method=='GET':
        T=Tasks.objects.filter(done=1)
        T.delete()
        return HttpResponseRedirect('/')





def recurring(request):
    #upddate progress
    p=len(Recurring.objects.filter(done=1)) + len(Tasks.objects.filter(done=1))
    try:
     d = Progress.objects.filter(date=tme)
     d.delete()
    except:
        pass
    #update progress
    obj = Progress(date=tme,progress=p)
    obj.save()
    
    #set done=0, if date stored in data's != today's date
    todays_date = str(dates)
    todays_date=int(todays_date.split(' ')[0].split('-')[2])
    #todays_date=int(todays_date[2])
    T=Recurring.objects.filter(date=todays_date)
    #if no data is present in the table with today's date, then 
    #set date=today's date and done=0 in all data of table
    if len(T)==0:
        Recurring.objects.update(done = 0)
        Recurring.objects.update(date=todays_date)
    T=Recurring.objects.all()
    return render(request,'Recurring.html',{'time':date,'T':T,'H':h})

def R_add(request):
    if request.method=='GET':
        h=1
        fm=R_Add_Task()  
    else:
        h=0
        fm=R_Add_Task(request.POST)
        if fm.is_valid():
            fm.save()
            fm=R_Add_Task() 
    T=Recurring.objects.all()
    return render(request,'Recurring.html',{'time':date,'T':T,'form':fm,'H':h})

def R_delete(request,id):
    if request.method=='POST':
        d = Recurring.objects.get(pk=id)
        d.delete()
        return HttpResponseRedirect('/recurring')
  

def R_update(request,id):
    if request.method=='POST':
        h=1
        u = Recurring.objects.get(pk=id)
        upd= R_Add_Task(request.POST,instance=u)
        if upd.is_valid():
            upd.save()
            return HttpResponseRedirect('/recurring')
    else:
        h=0
        u = Recurring.objects.get(pk=id)
        upd= R_Add_Task(instance=u)
    T=Recurring.objects.all()
    tiu=Recurring.objects.get(pk=id)
    return render(request,'update.html',{'time':date,'T':T,'form':upd,'H':h,'ti':tiu})

def R_finished(request,id):
    if request.method=='GET':
        #if done=1, set it to 0
        #ELSE, set it to 1
        #Tasks.objects.filter(pk=id).update(done = 1)
        T=Recurring.objects.get(pk=id)
        if T.done==0:
            Recurring.objects.filter(pk=id).update(done = 1)
        else:
            Recurring.objects.filter(pk=id).update(done = 0)
        return HttpResponseRedirect('/recurring')

def R_delete_all(request):
    if request.method=='GET':
        T=Recurring.objects.all()
        T.delete()
        return HttpResponseRedirect('/recurring')

def R_clear_finished(request):
    if request.method=='GET':
        T=Recurring.objects.filter(done=1)
        T.delete()
        return HttpResponseRedirect('/recurring')

def progress(request):
    if request.method=='GET':
        T=Progress.objects.all()
        C=Chartcolor.objects.all()
        xValues=[]
        yValues=[]
        for i in T:
            xValues.append(i.date)
            yValues.append(i.progress)
        xValues=xValues[-7:]
        yValues=yValues[-7:]
        return render(request,'progress.html',{'time':date,'xVal':xValues,'yVal':yValues,'color':C[0].color})

def changechartcolor(request,color):
    if request.method=='GET':
        C=Chartcolor.objects.all()
        C.delete()
        upd=Chartcolor(color=color)
        upd.save()
        return HttpResponseRedirect('/progress')

def timer(request):
    if request.method=='GET':
        #fetch the value of set timer from Timer table
        T=Timer.objects.all()
        #Time is in seconds
        Time=T[0].time
        if Time < 60:
            min='00'
            sec=Time
        else:
            min=int(Time/60)
            
            sec=int(Time%60)
        if sec<10:
                sec = str(sec)
                sec = '0'+ sec
        return render(request,'timer.html',{'Time_Val':Time,'Min':min,'Sec':sec})
    else:
        try:
         hr=int(request.POST['hr'])
        except:
          hr=0
        try:
         min=int(request.POST['min'])
        except:
          min=0
        try:
         sec=int(request.POST['sec'])
        except:
         sec=0
        #calculate in seconds
        tme=hr*60*60 + min*60 + sec

        print(tme)
        #push this data in Timer table
        T=Timer.objects.all()
        T.delete()
        T=Timer(time=tme)
        T.save()
        return HttpResponseRedirect('/timer')
      



        

