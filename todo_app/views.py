from django.http.response import HttpResponsePermanentRedirect,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from datetime import date
import calendar
from .forms import Add_Task,R_Add_Task
from django.contrib.auth.models import User,auth
from django.contrib.staticfiles.storage import staticfiles_storage

from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from os import listdir
from os.path import isfile, join
from django.core.files.storage import default_storage
from django.contrib import messages



from todo_app.models import Chartcolor, Progress, Tasks,Recurring, Timer,Audio
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
    ttl=len(Recurring.objects.all()) + len(Tasks.objects.all())
    #in try: check if todays data is available or not, if yes then delete the data.
    try:
     d = Progress.objects.filter(date=tme)
     d.delete()
    except:
        pass
    #enter new data of today
    #update progress
    obj = Progress(date=tme,progress=p,total=ttl)
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
    return HttpResponse("<h1>Hello World</h1>")
    '''
    if request.method=='GET':
        try:
          T=Progress.objects.all().order_by('id')
        except:
          T=Progress.objects.all()
        C=Chartcolor.objects.all()
        xValues=[]
        yValues=[]
        zValues=[]
        for i in T:
            xValues.append(i.date)
            yValues.append(i.progress)
            zValues.append(i.total)
        try:
            xValues=xValues[-7:]
            yValues=yValues[-7:]
            zValues=zValues[-7:]
        except:
            u=3
        return render(request,'progress.html',{'time':date,'xVal':xValues,'yVal':yValues,'zVal':zValues,'color':C[0].color}) '''

def changechartcolor(request,color):
    if request.method=='GET':
        C=Chartcolor.objects.all()
        C.delete()
        upd=Chartcolor(color=color)
        upd.save()
        return HttpResponseRedirect('/progress')


def changeaudio(request,audio_number):
    if request.method=='GET':
        C=Audio.objects.all()
        C.delete()
        upd=Audio(audio_number=audio_number)
        upd.save()
        return HttpResponseRedirect('/timer')

def timer(request):
    if request.method=='GET':
        #fetch the value of set timer from Timer table
        T=Timer.objects.all()
        #lets store all audio in a file:
        #any from database we will get the index and that index audio will be sent to timer page.
        aud_list = ['TGSZM2N-old-alarm-clock.mp3','y2mate-com-scam-1992-bgm-52384.mp3','y2mate-com-harry-potter-ringtone-bgm-tone-54095.mp3','sultan-abdul-hamid-music125165-52996.mp3','kgf-bgm-ringtone-44262.mp3','titanic-20romantic-23691.mp3']
        #trying to access the media files uploaded by user from media folder
        media_path = settings.MEDIA_ROOT
        myfiles = [f for f in listdir(media_path) if isfile(join(media_path, f))]
        #trim the name of audio files in myfiles
        
        custom_aud=[]
        for i in myfiles:
            custom_aud.append('/media/'+i)
            

        index=Audio.objects.all()[0].audio_number
        try:
          aud = staticfiles_storage.url(aud_list[index])
        except:
          aud=custom_aud[index-6]

        temp=[]
        global vmp
        vmp=myfiles
        for i in myfiles:
            a=i[:-4]
            temp.append(a[:12] if len(a)>12 else a)
        myfiles=temp
        audio_name =['Bell','Scam 1992', 'Harry Potter','Drive Forever','KGF','Titanic']
        audio_name+=myfiles
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
        return render(request,'timer.html',{'Time_Val':Time,'Min':min,'Sec':sec,'Aud':aud,'time':date,'Index':index,'Aud_name':audio_name,'Cust_name':myfiles})
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
      



        
def simple_upload(request):
    if request.method == 'POST' and request.FILES.get('myfile', False):
        myfile = request.FILES['myfile']
        #provide limit of 3 files to be added, if more than 3 is addded, pass a message to user
        media_path = settings.MEDIA_ROOT
        myfiles = [f for f in listdir(media_path) if isfile(join(media_path, f))]
    
        if myfile.name[-3:] == 'mp3':
            if len(myfiles) <=2 :
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
            else:
                messages.info(request,'There is a limit of 3 custom audio files. Delete 1 to add this.')
                #send the message in timer that "Its not an audio file."
            #uploaded_file_url = fs.url(filename)
        else:
            messages.info(request,'It is not an audio file.')
    return HttpResponseRedirect('/timer')

def delete_audio(request,num):
    #when any delete request is made, set the audio_index in Audio database to 0.
    changeaudio(request,0)
    #now delete the audio number passed from media folder
    default_storage.delete('/Users/DCQUASTER JACK/projects/todo/media/'+vmp[6-num])
    
    return HttpResponseRedirect('/timer')
