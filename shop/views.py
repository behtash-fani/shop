from django.shortcuts import render, get_object_or_404
from .models import MainCategory, Product
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views import View
from cart.forms import CartAddForm
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from wishlist.models import WishList
from django.conf import settings
from django.db.models import Q



class HomePage(View):
    products = Product.objects.filter(available=True)[:8]
    context = {'products':products}
    def get(self, request, *args, **kwargs):
        return render(request,'home.html', self.context)


class AboutUsView(TemplateView):
    template_name = 'about_us.html'

class ContactUsView(TemplateView):
    template_name = 'contact_us.html'


class FooterInformationView(View):
    template_name = 'base.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = MainCategory.objects.all()
        return context

class CategoryProductListView(ListView):
    model = Product
    template_name = 'shop/category_product_list.html'
    paginate_by = 9

    def get_queryset(self, *args, **kwargs):
        queryset = super(CategoryProductListView, self).get_queryset()
        category = get_object_or_404(MainCategory, slug=self.kwargs['slug'])
        return Product.objects.filter(available=True, maincategory=category).order_by('-created')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(MainCategory, slug=self.kwargs['slug'])
        context['category'] = get_object_or_404(MainCategory, slug=self.kwargs['slug'])
        return context

class ProductDetailView(FormMixin, DetailView):
    model = Product
    context_object_name = 'product'
    form_class = CartAddForm
    success_url = reverse_lazy('cart:detail')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        wishlist_product = []
        if self.request.user.is_authenticated:
            user_wishlist = WishList.objects.filter(user=self.request.user)
            for item in user_wishlist:
                for product in item.products.all():
                    wishlist_product.append(product.name)
        context['wishlist_product'] = wishlist_product
        return context


class SearchProductListView(ListView):
    template_name = 'shop/search_list.html'
    context_object_name = 'searched_products'
    paginate_by = 9

    def get_queryset(self):
        search = self.request.GET.get('q', default="")
        return Product.objects.filter(Q(name__icontains=search) | Q(description__icontains=search))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q')
        return context
    
class LowPriceProductsView(ListView):
    model = Product
    template_name = 'shop/category_product_list.html'
    paginate_by = 9

    def get_queryset(self, *args, **kwargs):
        queryset = super(LowPriceProductsView, self).get_queryset()
        category = get_object_or_404(MainCategory, slug=self.kwargs['slug'])
        return Product.objects.filter(available=True, maincategory=category).order_by('price')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(MainCategory, slug=self.kwargs['slug'])
        context['category'] = get_object_or_404(MainCategory, slug=self.kwargs['slug'])
        context['sorting'] = "Low - High Price"
        return context

class HighPriceProductsView(ListView):
    model = Product
    template_name = 'shop/category_product_list.html'
    paginate_by = 9

    def get_queryset(self, *args, **kwargs):
        queryset = super(HighPriceProductsView, self).get_queryset()
        category = get_object_or_404(MainCategory, slug=self.kwargs['slug'])
        return Product.objects.filter(available=True, maincategory=category).order_by('-price')
        
    def get_context_data(self, **kwargs):
        context  = super().get_context_data(**kwargs)
        category = get_object_or_404(MainCategory, slug=self.kwargs['slug'])
        context['category'] = get_object_or_404(MainCategory, slug=self.kwargs['slug'])
        context['sorting'] = "High - Low Price"
        return context


class AZNameProductsView(ListView):
    model = Product
    template_name = 'shop/category_product_list.html'
    paginate_by = 9

    def get_queryset(self, *args, **kwargs):
        queryset = super(AZNameProductsView, self).get_queryset()
        category = get_object_or_404(MainCategory, slug=self.kwargs['slug'])
        return Product.objects.filter(available=True, maincategory=category).order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(MainCategory, slug=self.kwargs['slug'])
        context['category'] = get_object_or_404(MainCategory, slug=self.kwargs['slug'])
        context['sorting'] = "A - Z Order"
        return context


class ZANameProductsView(ListView):
    model = Product
    template_name = 'shop/category_product_list.html'
    paginate_by = 9

    def get_queryset(self, *args, **kwargs):
        queryset = super(ZANameProductsView, self).get_queryset()
        category = get_object_or_404(MainCategory, slug=self.kwargs['slug'])
        return Product.objects.filter(available=True, maincategory=category).order_by('-name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(MainCategory, slug=self.kwargs['slug'])
        context['category'] = get_object_or_404(MainCategory, slug=self.kwargs['slug'])
        context['sorting'] = "Z - A Order"
        return context