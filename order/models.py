from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    picture_path = models.CharField(max_length=200)

class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)

class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item_id = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
