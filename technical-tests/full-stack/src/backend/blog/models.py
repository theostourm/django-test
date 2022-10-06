from django.db import models

class Post(models.Model):
    slug = models.TextField(unique=True, blank=True, null=True)
