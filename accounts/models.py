from django import forms
from django.db import models
from django.contrib.auth.models import AbstractUser
from . managers import CustomUserManager
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

class User(AbstractUser):
    pic = models.ImageField(upload_to = 'profile_picture', null=True, blank = True,
    default='profile_picture/defult.jpg'
    )  #فایل های عکسی پردازششون با پیلو هست
    bio = models.TextField(null = True , blank = True)
    job = models.CharField(max_length=100, null = True , blank = True)
    location = models.CharField(max_length=500, default='location', null = True , blank = True)
    objects = CustomUserManager()

    def get_absolute_url(self):
        return reverse("profile", kwargs={"username": self.username})


class SocialMedia(models.Model):
    KINDS = (
        ('w', 'web'),
        ('t', 'twiter'),
        ('f', 'facebook'),
        ('l', 'linkdin'),
        ('i', 'instagram'),
    )
    url = models.URLField()
    kinds = models.CharField(max_length = 1, choices = KINDS)
    user = models.ForeignKey(User,on_delete=models.CASCADE,)


class Skill(models.Model):
    name = models.CharField(max_length = 100)
    user = models.ManyToManyField(User)


class AddProfile(models.Model):
    pic = models.ImageField(null=True, blank = True,upload_to = 'profile_picture', default='profile_picture/defult.jpg')
    job = models.CharField(max_length=200)
    company = models.CharField(max_length=200, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    location = models.CharField(max_length=200)
    skills = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='profile')


class Experience(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=150)
    location = models.CharField(max_length=500)
    from_date = models.DateField()
    to_date = models.DateField()
    job_description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE) 


# user = get_user_model()

