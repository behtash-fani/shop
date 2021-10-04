from django.shortcuts import get_object_or_404
from .models import MainCategory, Product
from wishlist.models import WishList
from django.views.generic import ListView
from cart.sessions import Cart

def global_context(request):
    wishlist_item_count = 0
    if request.user.is_authenticated:
        wishlist_item = WishList.objects.filter(user=request.user)
        for item in wishlist_item:
            for product in item.products.all():
                wishlist_item_count += 1
    #fetch all cart items
    cart = Cart(request)
    item_count = 0
    for item in cart:
        item_count += 1
    #fetch all catogories
    products = Product.objects.all()
    categories = MainCategory.objects.all()
    context = {
        'categories': categories,
        'cart':cart,
        'item_count' : item_count,
        'wishlist_item_count':wishlist_item_count
    }
    return context
