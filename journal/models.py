from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    category_title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.category_title


class Post(models.Model):
    author = models.ForeignKey('auth.User', models.CASCADE)
    title = models.CharField(max_length=600)
    slug = models.SlugField(max_length=100, unique=True)
    text = RichTextField()
    categories = models.ManyToManyField(Category)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
