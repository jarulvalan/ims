from django.db import models
from decimal import Decimal
from datetime import datetime

class Product(models.Model):
    name = models.CharField(max_length=200)
    cetagory = models.CharField(max_length=200)
    supplier = models.CharField(max_length=200)
    unit_price = models.FloatField()
    quantity = models.PositiveIntegerField()
    date=models.DateTimeField(default=datetime.now())
    description = models.TextField(blank=True, null=True)

class incoming(models.Model):
    name = models.CharField(max_length=200)
    cetagory = models.CharField(max_length=200)
    supplier = models.CharField(max_length=200)
    unit_price = models.FloatField()
    quantity = models.PositiveIntegerField()
    date=models.DateTimeField(default=datetime.now())
    description = models.TextField(blank=True, null=True)
    
class outgoing_supply(models.Model):
    product_id=models.PositiveIntegerField()
    engg_name=models.CharField(max_length=200)
    #name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    date=models.DateTimeField(default=datetime.now())

    def __str__(self):
        return 'Id:{0} Name:{1}'.format(self.id, self.name)
        