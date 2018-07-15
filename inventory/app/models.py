from django.db import models
from aldjemy.meta import AldjemyMeta

class Brand(models.Model):
    name = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=255)

class Item(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

class Variant(models.Model):
    name = models.CharField(max_length=255)
    costprice = models.FloatField()
    sellngprice = models.FloatField()
    quantity = models.IntegerField()
    properties = models.CharField(max_length=255)
