from django.shortcuts import get_object_or_404, render
from .models import Post, Comment,Sample
# Create your views here.


def index(request):
    return render(request, 'blog/index.html', {})


def login(request):
    return render(request, 'blog/login.html', {})


def posts(request):
    if request.method == "POST":
        t = request.POST.get("title")
        b = request.POST.get("body")
        if t and b:
            p = Post(title = t, body = b)
            p.save()
    p = Post.objects.all()[:20]
    return render(request, 'blog/posts.html', {
        'posts': p,
    })


def post(request, id):
    # p = Post.objects.filter(id=id).first()
    p = get_object_or_404(Post, id=id)
    if request.method == "POST":
        comment = request.POST.get("text")
        if comment:
            c = Comment(body = comment, post=p)
            c.save()
    c = Comment.objects.filter(post=p)
    return render(request, 'blog/post.html', {
        'post': p,
        'comments': c,
        'username': 'MohammadNpak'
    })


def sample(request):
    if request.method == 'GET':
        return render(request, 'blog/sample.html', {
            'type': request.method
        })
    elif request.method == 'POST':
        input_text = request.POST["input"]
        sp = Sample(title = input_text)
        sp.save()
        return render(request, 'blog/sample.html', {
            'message':'your data has been saved!'
            })

