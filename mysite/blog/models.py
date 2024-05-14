# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    # Adding a many to  one relationship (user <---> posts)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, 
                               on_delete=models.CASCADE, 
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now) #publish  used python datetime now
    created = models.DateTimeField(auto_now_add=True) # created field
    updated = models.DateTimeField(auto_now=True) # updated field
    status = models.CharField(max_length=2, 
                              choices=Status, 
                              default=Status.DRAFT) #status field
    #The sorting is defined in a class - Meta to sort by publish field
    class Meta:
        ordering = ['-publish']
        #Adding indexes in descending (- before field publish)
        indexes = [
            models.Index(fields=['-publish']),
        ]
    def __str__(self):
        return self.title
    
