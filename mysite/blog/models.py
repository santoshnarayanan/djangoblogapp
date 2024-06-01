# Create your models here.
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes =[
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'

class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Post.Status.PUBLISHED)
        )


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    # Adding a many-to-one relationship (user <---> posts)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)  # publish  used python datetime now
    created = models.DateTimeField(auto_now_add=True)  # created field
    updated = models.DateTimeField(auto_now=True)  # updated field
    status = models.CharField(max_length=2,
                              choices=Status,
                              default=Status.DRAFT)  # status field
    # The sorting is defined in a class - Meta to sort by publish field
    objects = models.Manager()  # The default manager
    published = PublishedManager()  # Our custom manager
    tags = TaggableManager()

    class Meta:
        ordering = ['-publish']
        # Adding indexes in descending (- before field publish)
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', 
                       args=[
                           self.publish.year, 
                           self.publish.month, 
                           self.publish.day, 
                           self.slug
                           ])
