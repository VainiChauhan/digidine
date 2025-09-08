from django.shortcuts import render, get_object_or_404
from .models import Restaurant, Menu

def restaurant_menu(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    menu_items = Menu.objects.filter(restaurant=restaurant)
    return render(request, 'menu/restaurant_menu.html', {'restaurant': restaurant, 'menu_items': menu_items})
