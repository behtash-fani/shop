from .models import ArticleCategory

def article_context(request):
    article_categories = ArticleCategory.objects.all()
    context = {
        'article_categories': article_categories,
    }
    return context
