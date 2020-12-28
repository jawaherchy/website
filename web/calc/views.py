from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime
from calc.models import Contact
from django.contrib import messages
#for login page
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.
#now login logout work
# password for test user is 
# Create your views here.

    

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return redirect("/contact")
            #return render(request, 'base.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

    
def index(request):
    

    context ={
        'varriable':"this is sent"
    }
    return render(request,'index.html',context)


def services(request):
    
    return render(request,'services.html')


def travello(request):
    
    return render(request,'travello.html')


def about(request):
    
    return render(request,'about.html')


def contact(request):
    #for login
    print(request.user)
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            desc = request.POST.get('desc')
            contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
            contact.save()
            messages.success(request, 'Your message has been sent!')
        return render(request, 'contact.html')
    else:
        return redirect('/login')
