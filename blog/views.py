from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView
from .models import Article, ArticleCategory



class AllArticleListView(ListView):
    template_name = 'blog/article_list.html'
    model = Article
    paginate_by = 9

    def get_queryset(self):
        return Article.objects.filter(status="p").order_by('-created_at')

class CategoryArticleListView(ListView):
    template_name = 'blog/article_list.html'
    model = Article
    paginate_by = 9

    def get_queryset(self, *args, **kwargs):
        queryset = super(CategoryArticleListView, self).get_queryset()
        category = get_object_or_404(ArticleCategory, slug=self.kwargs['slug'])
        return Article.objects.filter(category=category , status="p").order_by('-created_at')


class SingleArticleView(DetailView):
    template_name = 'blog/article_detail.html'
    model = Article
    context_object_name = 'article_detail'
