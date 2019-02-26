from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    picture_path = models.CharField(max_length=200)

