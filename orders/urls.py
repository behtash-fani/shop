from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('create/', views.order_create, name='create'),
    path('payment/<int:order_id>/', views.order_detail, name='detail'),
    path('request/<int:order_id>/<price>', views.send_request, name='request'),
    path('verify/', views.verify , name='verify'),
]