from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('handyman.urls')),
    path('', include('django.contrib.auth.urls')),
]
