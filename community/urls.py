from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('api/', include('projects.urls')),
    path('', include('notification.urls')),
]
