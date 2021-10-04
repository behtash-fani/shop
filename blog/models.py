from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils.html import format_html



class ArticleCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    status = models.BooleanField(default=True, verbose_name='Show?')
    position = models.IntegerField()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('position',)
    def __str__(self):
        return self.title

class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    title = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ManyToManyField(ArticleCategory)
    description = models.TextField(blank=True, null=True)
    short_description = models.TextField(max_length= 200, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='blog_thumbnail/%Y/%m/%d/')
    images = models.ImageField(upload_to='blog_images/%Y/%m/%d/', null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)


    def __str__(self):
        return self.title
    
    def thumbnail_tag(self):
        return format_html("<img width=100 style='border-radius:5px' src='{}'>".format(self.thumbnail.url))
    thumbnail_tag.short_description = 'thumbnail'