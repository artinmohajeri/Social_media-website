from django.shortcuts import render
from .forms import AddExperienceForm
from .models import AddExperience
# Create your views here.


def register(request):
    return render(request, 'accounts/register.html', {})


def profile(request):
    return render(request, 'accounts/profile.html', {})


def add_exp(request):
    if request.method == "POST":
        form = AddExperienceForm(request.POST)
        if form.is_valid():
            form.save()
    form = AddExperienceForm()
    #     job_title = request.POST["title"]
    #     company = request.POST["company"]
    #     location = request.POST["location"]
    #     from_date = request.POST["from"]
    #     to_date = request.POST["to"]
    #     job_description = request.POST["description"]

    #     AD = AddExperience(job_title=job_title, company=company, location=location,from_date=from_date,to_date=to_date,job_description=job_description)

    #     AD.save()
    return render(request,
              'accounts/add-exp.html',
              {
                'form':form
                # "job_title" : job_title,
                # "company" : company,
                # "location" : location,
                # "from_date" : from_date,
                # "to_date" : to_date,
                # "job_description" : job_description,
              })


def create_profile(request):
    return render(request, 'accounts/create-profile.html', {})
