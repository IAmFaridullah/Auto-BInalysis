from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import client_details, clients_login
##from django.contrib.sessions.models import Session
##from django.contrib.sessions.backends.db import SessionStore

from django.template import loader, RequestContext
# Create your views here.


def index(request):
    return render(request, "userauthentication/index.html")


def Login_Page(request):
    return render(request, "userauthentication/Login.html")


def SignUp_Page(request):
    return render(request, "userauthentication/SignUp.html")


def SignUp_success(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('name') and request.POST.get('country') and request.POST.get('city') and request.POST.get('Accountname') and request.POST.get('email') and request.POST.get('password') and request.POST.get('gender') and request.POST.get('store'):
            cd = client_details()
            cl = clients_login()
            cd.Username = request.POST.get('username')
            cd.Org_Name = request.POST.get('name')
            cd.Org_Country = request.POST.get('country')
            cd.Org_City = request.POST.get('city')
            cd.Account_Name = request.POST.get('Accountname')
            cd.Email = request.POST.get('email')
            cd.Pswd_Hash = request.POST.get('password')
            cd.Client_Gender = request.POST.get('gender')
            cd.Client_Type = request.POST.get('store')

            cl.Username = request.POST.get('username')
            cl.Password = request.POST.get('password')
            cl.Client_Type = request.POST.get('store')

            cd.save()
            cl.save()

            print(cl.Username + "Data Insert Sucessful")
            print(cd.Username + "Sign Up Sucessful")
            return render(request, 'userauthentication/Login.html')
        else:
            return render(request, "userauthentication/SignUp.html")


def User_Dashboard(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password'):
            Username = request.POST.get('username')
            Password = request.POST.get('password')
            user = clients_login.objects.filter(
                Username=Username, Password=Password)
            if user.exists():
                ##session = SessionStore()
                # session.create()
                # session.save()
                ##request.session = session
                ##request.session['username'] = 'username'
                ##value = request.session.get('username', 'null')
                # request.session.clear()
                print(Username + "Logged In Sucessfully")
                return render(request, 'userauthentication/user_dashboard.html')
            else:
                return render(request, 'userauthentication/Login.html', {'error_message': 'Invalid username or password'})
