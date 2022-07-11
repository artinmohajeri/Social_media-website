from django.urls import path
from . import views

urlpatterns = [
    path("profile/",views.profile,name="profile"),
    path("login/",views.login_func,name="login"),
    path("register/",views.register,name="register"),
    path("create_profile/",views.create_profile,name="create_profile"),
    path("add_experience/",views.add_exp,name="add_experience"),
]
