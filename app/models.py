from django.db import models
from aldjemy.meta import AldjemyMeta

class Brand(models.Model):
    brand_name = models.CharField(max_length=255)

    def __str__(self):
        return self.brand_name

    __meta__ = AldjemyMeta

class Category(models.Model):
    category_name = models.CharField(max_length=255)

    __meta__ = AldjemyMeta

class Item(models.Model):
    item_name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    __meta__ = AldjemyMeta

class Variant(models.Model):
    variant_name = models.CharField(max_length=255)
    costprice = models.FloatField()
    sellingprice = models.FloatField()
    quantity = models.IntegerField()
    properties = models.CharField(max_length=255)

    __meta__ = AldjemyMeta
