from django.contrib import admin
from django.urls import path, include
from user.views import Register
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('saler_channel/', include('saler_channel.urls')),
    path('login/', auth_views.LoginView.as_view(template_name = 'user/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'user/logout.html'), name = 'logout'),
    path('register/', Register.as_view(), name = 'register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
