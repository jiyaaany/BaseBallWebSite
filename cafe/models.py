import os
from django.db import models
from django.utils import timezone
from uuid import uuid4

# Create your models here.
class Post(models.Model):
    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # title = models.CharField(max_length=200)
    # photo = models.ImageField(blank=True)
    # text = models.TextField()
    # create_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(auto_now_add=True)
    # title = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    # body = models.TextField()
    title = models.CharField(max_length=64, verbose_name="제목")
    file = models.FileField(null=True)
    # content = models.TextField(verbose_name="내용")

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.title
