from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from . models import Order, OrderItem
from meny.models import Item

def order(request):
    new_order = Order()
    new_order.save() 
    item_id = []
    item_counter = []

    for key, values in request.POST.lists():
        if key == 'item_id':
            item_id = values
        elif key == 'count':
            item_counter = values
    
    for i in range(0, len(item_id)):
        if item_counter[i] != '':
            item = Item.objects.get(pk=item_id[i])
            counter = int(item_counter[i])
            for j in range(0, counter):
                order_item = OrderItem(order_id=new_order, item_id=item)
                order_item.save()



    item_info = zip(item_id, item_counter)
    context = {'item_info':item_info}
    return render(request, 'order/order_items.html', context)
