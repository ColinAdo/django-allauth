from django.shortcuts import render, redirect
from django.contrib.auth import logout

def home(request):
    template = 'users/index.html'
    return render(request,template)

def login(request):
    template = 'users/login.html'
    return render(request,template)

def logout_view(request):
    logout(request)
    return redirect('login')
