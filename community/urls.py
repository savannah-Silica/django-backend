from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('', include('api.urls')),
    path('', include('projects.urls')),
    path('', include('notification.urls')),
]
