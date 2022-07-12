from django import forms
from .models import Experience,User,SocialMedia,Skill, Register

class AddExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        exclude = ['user']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = []

class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = SocialMedia
        exclude = ['user']

class SkillSetForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['name','username','password']