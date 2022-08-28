from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

user = get_user_model()
class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(user, on_delete=models.CASCADE)
    likes = models.ManyToManyField(user, related_name="blog_posts")
    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("post", kwargs={"id": self.id})

    def __str__(self) -> str:
        return f"{self.title}  |  {self.body[:20]}"


class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(user, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.body[:30]}"

class Sample(models.Model):
    title = models.CharField(max_length=100)

# class LikePost(models.Model):
#     post_id = models.CharField(max_length=1000)
#     username = models.CharField(max_length=200)



