from django.db import models

# Create your models here.
(from django.db import models

# Create your models here.
class Item(models.Models):
	name = models.CharField()
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	category = models.ManyToManyField(Category)


class Variant(models.Model):
	name = models,CharField()
	costprice = models.FloatField()
	sellngprice = models.FloatField()
	quantity = models.IntegerField()
	properties = models.CharField()

class Brand(models.Model):
	name = models.CharField()

class Category(models.Model):
	name = models.CharField()




