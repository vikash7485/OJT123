from django.contrib import admin
from .models import Category, Article, ReadLater


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'source', 'category', 'published_at']
    list_filter = ['category', 'published_at']
    search_fields = ['title', 'description', 'source']
    readonly_fields = ['created_at']


@admin.register(ReadLater)
class ReadLaterAdmin(admin.ModelAdmin):
    list_display = ['user', 'article', 'added_at']
    list_filter = ['added_at']
    search_fields = ['user__username', 'article__title']

