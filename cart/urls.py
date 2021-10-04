from django.urls import path
from . import views


app_name = 'cart'
urlpatterns = [
    path('', views.CartDetailView.as_view() , name='cart_detail'),
    path('add/<int:product_id>', views.cart_product_add, name='card_add'),
    path('addtocart/<int:product_id>', views.add_to_cart, name='card_to_add'),
    path('remove/<int:product_id>', views.cart_product_remove, name='card_remove'),
]
