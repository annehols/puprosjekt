from django.urls import path

from . import views
from order import views as orderViews

app_name = 'meny'

urlpatterns = [
    path('', views.meny_items, name='meny_items'),
]
