from django.db import models

# Create your models here.

from django.utils import timezone

class Post(models.Model):
    title=models.CharField(max_length=256)
    slug=models.SlugField()
    body=models.TextField()
    pub_date=models.DateTimeField(default=timezone.now)
    like_count=models.IntegerField(default=0)

    class Meta:
        ordering=('-like_count',)
    
    def __str__(self):
        return self.title

class Video(models.Model):
    title=models.CharField(max_length=256)
    slug=models.SlugField()
    src=models.CharField(max_length=256)
    pub_date=models.DateTimeField(default=timezone.now)

    class Meta:
        ordering=('-pub_date',)
    
    def __str__(self):
        return self.title