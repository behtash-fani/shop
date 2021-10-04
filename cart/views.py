from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from .sessions import Cart
from shop.models import Product
from .forms import CartAddForm
from django.views.decorators.http import require_POST


class CartDetailView(TemplateView):
    template_name = 'cart/cart.html'

@require_POST
def cart_product_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add_cart(product=product, quantity=cd['quantity'])
    return redirect('cart:cart_detail')

def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add_cart(product=product, quantity=1)
    return redirect('cart:cart_detail')

def cart_product_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove_cart(product)
    return redirect('cart:cart_detail')



    