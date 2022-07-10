from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from blog.forms import CommentForm, PostForm

from .models import Post, Comment, Sample
# Create your views here.


def index(request):
    return render(request, 'blog/index.html', {})


def login(request):
    return render(request, 'blog/login.html', {})

@login_required(login_url='/account/login/')
def posts(request):
    # u = get_user_model().objects.first()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid:
            form.save()
        # t = request.POST.get("title")
        # b = request.POST.get("body")
        # if t and b:
        #     p = Post(title = t, body = b)
        #     p.save()
    p = Post.objects.all()[:20]
    form = PostForm()
    return render(request, 'blog/posts.html', {
        'posts': p,
        'forms': form,
        # 'u':u,
    })

@login_required(login_url='/account/login/')
def post(request, id):
    # p = Post.objects.filter(id=id).first()
    p = get_object_or_404(Post, id=id)
    # u = get_user_model().objects.first()
    if request.method == "POST":
        comment = CommentForm(request.POST)
        if comment.is_valid:
            comment_object = comment.save(commit=False)
            comment_object.post = p
            comment_object.writer = request.user
            comment_object.save()
    form = CommentForm()
    # comment = request.POST.get("text")
    # if comment:
    #     c = Comment(body = comment, post=p)
    #     c.save()
    c = Comment.objects.filter(post=p)
    return render(request, 'blog/post.html', {
        'post': p,
        'comments': c,
        'form': form,
        # 'u': u,
    })


def sample(request):
    if request.method == 'GET':
        return render(request, 'blog/sample.html', {
            'type': request.method
        })
    elif request.method == 'POST':
        input_text = request.POST["input"]
        sp = Sample(title=input_text)
        sp.save()
        return render(request, 'blog/sample.html', {
            'message': 'your data has been saved!'
        })
