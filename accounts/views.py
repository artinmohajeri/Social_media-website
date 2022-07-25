from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import AddExperienceForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User,Experience,AddProfile



def register(request):
    if request.method == "POST":
        # name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username has already been taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                return redirect('login')
        else:
            messages.info(request, 'two passwords do not match!')
            return redirect('register')

    return render(request, 'accounts/register.html', {})


@login_required
def profile(request, username):
    user=get_object_or_404(User,username=username)    
    return render(request, 'accounts/profile.html', {'user':user})


@login_required
def add_exp(request):
    if request.method == "POST":
        title = request.POST['title']
        company = request.POST['company']
        location = request.POST['location']
        from_date = request.POST['from']
        to = request.POST['to']
        description = request.POST['description']
        if title and location and from_date and to:
            exp = Experience(job_title=title, company=company, from_date=from_date, location=location,to_date=to, job_description=description)
            exp.user = request.user
            # exp = exp.save(commit = False)
            exp.save()
            messages.SUCCESS(request, 'your experience has been saved!')
            return redirect(to=reverse('profile'))
        else:
            messages.info(request, ' fill out the form completly')
            return redirect('add-exp')

    return render(request, 'accounts/add-exp.html', {})


@login_required
def create_profile(request):
    # user_profile = AddProfile.objects.get(user=request.user)
    if request.method == "POST":
        job = request.POST['job']
        company = request.POST['company']
        website = request.POST['website']
        location = request.POST['location']
        skills = request.POST['skills']
        bio = request.POST['bio']
        # pic = request.POST['profilepic']
        if job and company and location and skills:
            pro = AddProfile(job=job, company=company, location=location, website=website, skills=skills, bio=bio, user=request.user)
            # pro.user = request.user
            pro.save()
            # return redirect('profile')

        else:
            messages.info(request, ' fill out the form completly')
            return redirect('create_profile')

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


def delete_exp(request, id):
    exp = get_object_or_404(Experience ,id=id)
    if exp.user == request.user:
        exp.delete()
        messages.add_message(request,messages.SUCCESS,"Your post has been deleted!")
        # return redirect(to=reverse('profile'))
    else:
        pass
    return render(request, "accounts/profile.html", {})

    