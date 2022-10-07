from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    author_1 = models.CharField(max_length=150)
    author_2 = models.CharField(max_length=150, blank=True)
    author_3 = models.CharField(max_length=150, blank=True)
    tags = models.ManyToManyField(Tag)
    image_url = models.URLField(max_length=500)
    image_description = models.TextField()

