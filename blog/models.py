from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from taggit.managers import TaggableManager
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'DRAFT'
        PUBLISHED = 'PB', 'PUBLISHED'

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    tags = TaggableManager()

    def __str__(self):
        return self.title
    
    # مهمة لمحركات البحث 
    def get_absolute_url(self):
            return reverse("blog:post-detail", args=[self.slug])
        
    class Meta:
        ordering = ['-pub_date']
        indexes = [
            models.Index(fields=['-pub_date']),
            models.Index(fields=['slug']),
        ]


class Comment(models.Model):
     post = models.ForeignKey(Post , on_delete=models.CASCADE, related_name='comments')
     name = models.CharField(max_length=80)
     email = models.EmailField()
     body = models.TextField()
     created = models.DateTimeField(auto_now_add=True)
     updated = models.DateTimeField(auto_now=True)
     active = models.BooleanField(default=True)

     class Meta:
          ordering = ['created']
          indexes = [
               models.Index(fields=['created']),
          ]

     def __str__(self):
      return f'Comment by {self.name} on {self.post.title}'

     