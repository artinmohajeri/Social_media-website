from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("posts/",views.posts,name="posts"),
    path("sample/",views.sample,name="sample"),
    path("post/<int:id>",views.post,name="post"),
    path('post/delete/<int:id>',views.delete_post ,name='delete_post'),
    path('comment/delete/<int:id>',views.delete_comment ,name='delete_comment'),
    # path("post/",views.post,name="post"),
]
