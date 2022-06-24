from django.shortcuts import render

# Create your views here.


def register(request):
    return render(request,'accounts/register.html',{})

def profile(request):
    return render(request,'accounts/profile.html',{})

def add_exp(request):
    return render(request,'accounts/add-exp.html',{})

def create_profile(request):
    return render(request,'accounts/create-profile.html',{})

