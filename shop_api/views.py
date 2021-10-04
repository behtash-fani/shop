from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from shop.models import Product

# class ProductListAPIView(ListAPIView):
# 	queryset = Product.objects.all()
# 	serializer_class = ProductSerializer
# 	permission_classes = [IsAuthenticated]

# class SingleProductAPIView(RetrieveUpdateDestroyAPIView):
# 	queryset = Product.objects.all()
# 	serializer_class = ProductSerializer
# 	permission_classes = [IsAuthenticated]


class ProductViewSet(ModelViewSet):
	queryset = Product.objects.all()
	filterset_fields = ['maincategory', 'subcategory', 'name', 'description', 'stock', 'available']
	serializer_class = ProductSerializer
	permission_classes = [IsAuthenticated]