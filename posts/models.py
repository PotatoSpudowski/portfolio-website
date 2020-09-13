from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



class Post(models.Model):
    title = models.CharField(max_length=250)
    overview = models.TextField()
    textbody = models.TextField()
    projecturl = models.TextField()
    # viewCount = models.IntegerField(default=1)
    # liveViewCount = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    img1 = models.ImageField(blank=True, null=True)
    img2 = models.ImageField(blank=True, null=True)
    img3 = models.ImageField(blank=True, null=True)
    img4 = models.ImageField(blank=True, null=True)
    img5 = models.ImageField(blank=True, null=True)
    featured = models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'id': self.id
        })

    @property
    def viewCount(self):
        return PostView.objects.filter(post=self).count()

