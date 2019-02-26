from django.shortcuts import render

from . models import Item

def meny_items(request):
    all_meny_items = Item.objects.order_by('-id')[:]
    context = {'all_meny_items':all_meny_items,}
    return render(request, 'meny/meny_items.html', context)
