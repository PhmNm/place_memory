from django.shortcuts import render, redirect
from django.contrib.auth import logout

def home(request):
    return render(request, 'myApp/home.html')

def dashboard(request):
    return render(request, 'myApp/dashboard.html')

def logoutHandle(request):
    logout(request)
    return redirect("/")