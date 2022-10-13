from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Products(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length = 200)
    description = models.TextField() #to fit more data hence charfield is not used
    image = models.CharField(max_length = 300)

class Order(models.Model):
    def __str__(self):
        return self.name
    items = models.CharField(max_length=2000)
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length=300)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    state = models.CharField(max_length=500)
    zip = models.CharField(max_length=500)
    total = models.CharField(max_length = 500)

     