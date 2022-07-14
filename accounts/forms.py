from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm

class AddExperienceForm(forms.ModelForm):
    class Meta:
        model = models.Experience
        exclude = ['user']

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         exclude = ['user']

class UserForm(UserCreationForm):
    class Meta:
        model=models.User
        fields=['username','email']

class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = models.SocialMedia
        exclude = ['user']

class SkillSetForm(forms.ModelForm):
    class Meta:
        model = models.Skill
        fields = ['name']

# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = Register
#         fields = ['name','username','password']