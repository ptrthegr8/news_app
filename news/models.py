from django.db import models
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    byline = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=150)
    post_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

