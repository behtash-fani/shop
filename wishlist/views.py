from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from django.views import View
from .models import WishList
from shop.models import Product
from django.conf import settings



class WishListView(ListView):
    model = WishList
    template_name = 'wishlist/wishlist_list.html'
    context_object_name = 'wishlist'


class AddWishListView(View):
    def get(self,request, *args, **kwargs):
        user = request.user
        product_id = self.kwargs['id']
        product_slug = self.kwargs['slug']
        product = get_object_or_404(Product, id = product_id)
        wishlist = get_object_or_404(WishList, user=user)
        wishlist.products.add(product)
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

class RemoveWishListView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        wishlist = get_object_or_404(WishList, user=user)
        for item in wishlist.products.all():
            if item.id == self.kwargs['id']:
                wishlist.products.remove(item)
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))