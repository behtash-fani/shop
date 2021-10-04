from django.urls import path, include
from .views import ProductViewSet
from rest_framework import routers



router = routers.SimpleRouter()
router.register('', ProductViewSet, basename='products')


urlpatterns = [
    path('', include(router.urls)),
]