from django.urls import path
from .views import WishListView, RemoveWishListView, AddWishListView


app_name = 'wishlist'
urlpatterns = [
    path('', WishListView.as_view(), name='wishlist'),
    path('add/<int:id>/<slug:slug>/', AddWishListView.as_view(), name='add_wishlist'),
    path('remove/<int:id>/', RemoveWishListView.as_view(), name='remove_wishlist'),
]
