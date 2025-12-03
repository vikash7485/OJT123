from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(max_length=1000)
    url_to_image = models.URLField(max_length=1000, blank=True, null=True)
    published_at = models.DateTimeField()
    source = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-published_at']
        indexes = [
            models.Index(fields=['-published_at']),
            models.Index(fields=['category']),
        ]
    
    def __str__(self):
        return self.title[:100]


class ReadLater(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'article']
        ordering = ['-added_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.article.title[:50]}"

