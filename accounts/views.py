from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from .forms import AddExperienceForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,"you have registered successfuly!")
            return redirect(to=reverse('login'))
        else:
            messages.add_message(request, messages.ERROR,"you date is not valid!")
            return render(request, 'accounts/register.html', {'form': form})

    elif request.method == "GET":
        form = UserForm()
        return render(request, 'accounts/register.html', {'form': form})
        
    else:
        return HttpResponse("404")


@login_required
def profile(request):
    # user = User.objects.get(id=id)
    return render(request, 'accounts/profile.html', {})


@login_required
def add_exp(request):
    if request.method == "POST":
        form = AddExperienceForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Your date has been saved!")
            # return redirect(to=reverse('profile'))
        else:
            print('Poor Artin')
            return render(request, 'accounts/add-exp.html', {'form': form})

    elif request.method == "GET":
        form = AddExperienceForm()
    else:
        return HttpResponse("404")

    return render(request, 'accounts/add-exp.html', {'form': form})


@login_required
def create_profile(request):
    # if request.method == "POST":
    #     form = ProfileForm(request.POST)
    #     if form.is_valid():
    #         form = form.save(commit=False)
    #         form.user = request.user
    #         form.save()
    #         messages.add_message(request, messages.SUCCESS,"Your date has been saved!")
    #         # return redirect(to=reverse('profile'))
    #     else:
    #         print('Poor Artin')
    #         return render(request,'accounts/add-exp.html',{'form':form})

    # elif request.method == "GET":
    #     form = ProfileForm()
    # else:
    #     return HttpResponse("404")
    return render(request, 'accounts/create-profile.html', {})


def login_func(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(to=reverse('create_profile'))
        else:
            messages.add_message(request, messages.ERROR,
                                 "username or password is not correct")
    return render(request, 'accounts/login.html', {})


def logout_func(request):
    logout(request)
    return redirect(to=reverse('index'))
