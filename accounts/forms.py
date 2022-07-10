from django import forms
from .models import AddExperience,User,SocialMedia,SkillSet

class AddExperienceForm(forms.ModelForm):
    class Meta:
        model = AddExperience
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
        model = SkillSet
        fields = ['name']