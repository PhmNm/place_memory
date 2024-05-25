from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'myApp/main.html')

@login_required
def dashboard(request):
    return render(request, 'myApp/dashboard.html')

def logoutHandle(request):
    logout(request)
    return redirect("/")