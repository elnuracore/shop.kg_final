from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

def logout_view(request):
    logout(request)
    return redirect('/')

urlpatterns = [
    path('admin/logout/', logout_view),
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('users/', include('users.urls')), 
    path('', include('products.urls')),    
    path('clothes/', include('clothes.urls')),
    # ДОБАВЬТЕ ЭТУ СТРОКУ (проверьте, что папка называется basket)
    path('basket/', include('basket.urls', namespace='basket')), 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)