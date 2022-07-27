from turtle import mode
from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.TextField()
    # slug is url encoded value
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)