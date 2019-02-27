from django.urls import path

from . import views

app_name = 'order'

urlpatterns = [
    path('order/all_orders/', views.all_orders, name='all_orders'),
    path('order/your_order/', views.your_order, name='your_order'),
    path('', views.order, name='order'),
]
