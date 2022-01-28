from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate

# Create your views here.
def login(request,backend='django.contrib.auth.backends.ModelBackend'):
    if request.method=='POST':
        try:
            username=request.POST['username']
            password= request.POST['password']
        except:
        #for google login
        #push the returned data in social accounts
            try:
                obj = User(request.POST['username'])
                obj.save()
            except:
                obj = User.objects.filter(username=request.POST['username']).first()
            #authenticate the user
            #user=authenticate(username=request.POST['username'])
            #auth.login(request,user)
            login(request, obj, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("index")


        user1=authenticate(username=username,password=password)
        user2=authenticate(email=username,password=password)
        user=user1 if user1 else user2
        if user:
            auth.login(request,user)
            return redirect("index")
        else:
            messages.info(request,'Invalid username or password')
            return redirect('login')
    else:
        return render(request,'login.html')   


def register(request):
    if request.method=='POST':
     try:
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        confirm_password= request.POST['confirmpassword']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            elif len(password)<4:
                messages.info(request,'Password should be at least 4 digits')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
        return redirect('/')
     except:
        messages.info(request,'Fields are empty')
        return redirect('register')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect("/")
    


