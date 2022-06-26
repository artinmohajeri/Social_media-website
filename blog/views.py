from django.shortcuts import get_object_or_404, render
from .models import Post,Comment
# Create your views here.


def index(request):
    return render(request,'blog/index.html',{})

def login(request):
    return render(request,'blog/login.html',{})

def posts(request):
    posts = Post.objects.all()[:20]
    return render(request,'blog/posts.html',{
        'posts':posts
    })

def post(request,id):
    # p = Post.objects.filter(id=id).first()
    p = get_object_or_404(Post,id=id)
    c = Comment.objects.filter(post=p)
    return render(request,'blog/post.html',{
        'post' : p,
        'comments' : c,
        'username':'MohammadNpak'
    })




