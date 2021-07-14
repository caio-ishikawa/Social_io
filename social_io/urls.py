from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('register/', include('main.urls')),
    path('login/', include('main.urls')),
    path('like/<int:pk>/', include('main.urls')),
    path('logout/', include('main.urls')),
    path('profile/edit/<int:pk>/', include('main.urls')),
    path('profile/p/<int:pk>/', include('main.urls')),
    path('post/delete/<int:pk>/', include('main.urls')),
    path('profile/follow/<int:pk>/', include('main.urls')),
    path('feed/following/', include('main.urls')),
    path('feed/trending/', include('main.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
