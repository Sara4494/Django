from django.contrib import admin
from app.models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(ShippngAddress)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Category)