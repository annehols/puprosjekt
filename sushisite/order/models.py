from django.db import models
from meny.models import Item 

class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True, blank=True)

class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    
