from django.contrib import admin
from django.urls import path, include, re_path
# from rest_framework_simplejwt import views as jwt_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Shop API",
      default_version='v1',
      description="All endpoints of this shop",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="support@shop.com"),
      license=openapi.License(name="GPLv3 License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    #all project apps urls
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('wishlist/', include('wishlist.urls', namespace='wishlist')),
    path('', include('shop.urls', namespace='shop')),
    path('blog/', include('blog.urls', namespace='blog')),
    #all api urls
    path('api-auth/', include('rest_framework.urls')),
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api/products/', include('shop_api.urls')),
    path('api/accounts/', include('accounts_api.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

