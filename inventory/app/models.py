from django.db import models
from aldjemy.meta import AldjemyMeta

class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    __meta__ = AldjemyMeta

class Category(models.Model):
    name = models.CharField(max_length=255)

    __meta__ = AldjemyMeta

class Item(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    __meta__ = AldjemyMeta

class Variant(models.Model):
    name = models.CharField(max_length=255)
    costprice = models.FloatField()
    sellingprice = models.FloatField()
    quantity = models.IntegerField()
    properties = models.CharField(max_length=255)

    __meta__ = AldjemyMeta
