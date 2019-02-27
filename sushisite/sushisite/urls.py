from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('order/', include('order.urls')),
    path('admin/', admin.site.urls),
]
