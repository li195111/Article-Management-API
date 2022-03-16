# article_manage/modles.py

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    
class Article(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=250)
    tags = models.CharField(max_length=250)
    thumbnail = models.URLField(max_length=1000)
    content = models.TextField(blank=True)
    publish_at = models.DateField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    