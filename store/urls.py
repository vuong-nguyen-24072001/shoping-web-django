from django.urls import path
from .views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Store.as_view(), name = 'store'),
    path('cart/', Cart.as_view(), name = 'cart'),
    path('product_api/', GetAllProductAPIView.as_view()),
    path('cart_item_api/', GetAllCartItemAPIView.as_view()),
    path('checkout/', CheckOut.as_view(), name = 'checkout'),
    path('update_item/', UpdateJson.as_view(), name = 'update_item'),
    path('product/<int:pk>', ProductDetaiView.as_view(), name = 'product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)