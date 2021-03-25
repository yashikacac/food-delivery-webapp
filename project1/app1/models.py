from django.db import models

# Create your models here.
class foodModel(models.Model):
    name = models.CharField(max_length = 10)
    price = models.CharField(max_length = 10)

class CustomerModel(models.Model):
    userid = models.CharField(max_length = 10)
    phoneno = models.CharField(max_length = 10)

class OrderModel(models.Model):
    username = models.CharField(max_length = 10)
    phoneno = models.CharField(max_length = 10)
    address = models.CharField(max_length = 10)
    orderitems = models.CharField(max_length = 10)
    orderstatus = models.CharField(max_length = 10, default="Pending")

