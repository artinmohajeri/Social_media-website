from django.contrib import admin
# Register your models here.
from . import models

from django.contrib import admin
from . import models
# Register your models here.


# admin.site.register(models.User)
# admin.site.register(models.AddProfile)

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(models.SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    pass 

@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass

# @admin.register(models.AddProfile)
# class AddProfileAdmin(admin.ModelAdmin):
#     pass




    
