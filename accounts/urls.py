from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    # user dashboard urls
    path('personal-info/', views.PersonalInfoView.as_view(), name='user_personal_info'),
    path('personal-info/<int:pk>/edit/', views.PersonalInfoEditView.as_view(), name='user_personal_info_edit'),
    path('wishlist/', views.WishListView.as_view(), name='user_wish_list'),
    path('products-purchased/', views.ProductsPurchasedView.as_view(), name='products_purchased'),
    path('api-info/', views.ApiView.as_view(), name='api_info'),
    # register login and logout urls
    path('login/', views.UserLoginView, name='user_login'),
    path('login/with-password/', views.user_login_pw, name='user_login_with'),
    path('login/with-code/', views.user_login_code, name='user_login_code'),
    path('login/with-code/verify/', views.login_verify_code, name='login_verify_code'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.user_register, name='user_register'),
    path('register/verify/', views.register_verify_phone, name='register_verify_phone'),    
]