from django.shortcuts import render, redirect
from django.http import JsonResponse

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *

def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'myApp/main.html')

@login_required
def logout_handle(request):
    logout(request)
    return redirect("/")

@login_required
def dashboard(request):
    memories = Memory.objects.filter(user=request.user)
    context = {'memories':memories}
    return render(request, 'myApp/dashboard.html', context)

@login_required
def load_memory(request):
    memories = Memory.objects.filter(user=request.user)
    data = list(memories.values('longitude', 'latitude', 'place_name', 'comments'))
    return JsonResponse(data, safe=False)

@login_required
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