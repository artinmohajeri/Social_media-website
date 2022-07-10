from django.contrib import admin
from .models import AddExperience,SocialMedia,SkillSet,User
# Register your models here.

from django.contrib import admin
from . import models
# Register your models here.


# admin.site.register(models.User)

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(models.SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    pass 

@admin.register(models.SkillSet)
class SkillAdmin(admin.ModelAdmin):
    pass

@admin.register(models.AddExperience)
class AddExperienceAdmin(admin.ModelAdmin):
    pass



    
