from django.contrib import admin

# Register your models here.
from .models import foodModel,CustomerModel,OrderModel

admin.site.register(foodModel)
admin.site.register(CustomerModel)
admin.site.register(OrderModel)