from django.db import models
from datetime import datetime

class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    full_text = models.TextField()
    category = models.CharField(max_length=30)
    pubdate = models.DateTimeField()
    # slug = ... todo
    # is_published = models.BooleanField()todo