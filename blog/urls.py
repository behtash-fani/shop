from django.urls import path
from .views import AllArticleListView, SingleArticleView, CategoryArticleListView

app_name = 'blog'
urlpatterns = [
    path('', AllArticleListView.as_view(), name='article_list'),
    path('c/<slug:slug>/', CategoryArticleListView.as_view(), name='category_article_list'),
    path('article/<slug:slug>/', SingleArticleView.as_view(), name='article_detail'),
]