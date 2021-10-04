from django.urls import path
from . import views
from . import context_processors


app_name = 'shop'
urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('p/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('search/', views.SearchProductListView.as_view(), name='product_search'),
    path('c/<slug:slug>/', views.CategoryProductListView.as_view(), name='category_product_list'),
    path('c/<slug:slug>/lowprice-products/', views.LowPriceProductsView.as_view(), name='lowprice'),
    path('c/<slug:slug>/highprice-products/', views.HighPriceProductsView.as_view(), name='highprice'),
    path('c/<slug:slug>/a-to-z-products/', views.AZNameProductsView.as_view(), name='a-to-z-name'),
    path('c/<slug:slug>/z-to-a-products/', views.ZANameProductsView.as_view(), name='z-to-a-name'),
    path('about-us', views.AboutUsView.as_view(), name='about-us'),
    path('contact-us', views.ContactUsView.as_view(), name='contact-us'),
]
