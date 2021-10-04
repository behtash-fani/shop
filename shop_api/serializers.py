from rest_framework import serializers
from shop.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','maincategory','subcategory','name','slug','image','description','price','stock','available']