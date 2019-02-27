from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from . models import MenuItem, Order, OrderItem

def order(request):
    all_menu_items = reversed(MenuItem.objects.order_by('-id')[:])
    context = {'all_menu_items':all_menu_items,}
    return render(request, 'order/menu_items.html', context)

def your_order(request):
    new_order = Order()
    new_order.save() 

    menu_item_id = []
    item_counter = []
    for key, values in request.POST.lists():
        if key == 'menu_item_id':
            menu_item_id = values
        elif key == 'count':
            item_counter = values    
            
    for i in range(0, len(menu_item_id)):
        if item_counter[i] != '':
            # Item is ordered by user
            menu_item = MenuItem.objects.get(pk=menu_item_id[i])
            counter = int(item_counter[i])
            for j in range(0, counter):
                order_item = OrderItem(order_id=new_order, menu_item_id=menu_item)
                order_item.save()
    item_info = zip(menu_item_id, item_counter)
    context = {'item_info':item_info, 'i':i}
    return render(request, 'order/your_order.html', context)


def all_orders(request):
    order_list = Order.objects.all()
    order_item_lists = []

    for order in order_list:
        order_item_lists.append(OrderItem.objects.filter(order_id=order))
    orders = zip(order_list, order_item_lists)
    context = {'orders':orders}
    return render(request, 'order/all_orders.html', context)
    pass

