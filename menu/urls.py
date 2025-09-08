from django.urls import path
from . import views

urlpatterns = [
    path('restaurant/<uuid:restaurant_id>/menu/', views.restaurant_menu, name='restaurant_menu'),
]