from django.shortcuts import render, redirect

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .forms import *

def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'myApp/main.html')

@login_required
def dashboard(request):
    return render(request, 'myApp/dashboard.html')

def logout_handle(request):
    logout(request)
    return redirect("/")

def new_memory(request):
    form = MemoryForm()
    if request.method == 'POST':
        form = MemoryForm(request.POST)
        if form.is_valid():
            memory = form.save(commit=False)
            memory.user = request.user
            memory.save()
            return redirect('dashboard')
    context = {'form':form}
    return render(request, 'myApp/new-memory.html', context)