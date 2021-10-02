from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name = 'user/login.html'), name = 'login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name = 'user/logout.html'), name = 'logout'),
    path('', Home.as_view(), name = 'saler_home'),
    path('profile_shop/', ProfileShopView.as_view(), name = 'saler_profile_shop'),
    path('manage/all_product', AllProduct.as_view(), name = 'saler_all_product'),
    path('manage/update_product/<int:pk>', UpdateProductView.as_view(), name = 'update_product'),
    path('manage/all_product/create_product', CreateProductView.as_view(), name = 'create_product'),
]
