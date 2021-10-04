from django.contrib import admin
from .models import Article, ArticleCategory
from django.contrib import messages
from django.utils.translation import ngettext

@admin.action(description='Publish selected articles')
def make_published(self, request, queryset):
    updated = queryset.update(status='p')
    self.message_user(request, ngettext(
        '%d article was successfully marked as published.',
        '%d articles were successfully marked as published.',
        updated,
    ) % updated, messages.SUCCESS)


@admin.action(description='Draft selected articles')
def make_drafted(self, request, queryset):
    updated = queryset.update(status='d')
    self.message_user(request, ngettext(
        '%d article was successfully marked as draft.',
        '%d articles were successfully marked as draft.',
        updated,
    ) % updated, messages.SUCCESS)


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'position',)
    search_fields = ('title',)
    list_filter = ('title', 'status')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_tag', 'publish', 'created_at', 'updated', 'status', 'category_to_str')
    search_fields = ('title', 'description')
    list_filter = ('title', 'status')
    prepopulated_fields = {'slug': ('title',)}
    actions = [make_published, make_drafted]

    def category_to_str(self, obj):
        return ", ".join([category.title for category in obj.category.all()])
    category_to_str.short_description = 'Category'
