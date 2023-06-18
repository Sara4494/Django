from django.contrib import admin

# Register your models here.
from app.models import *
 

 
class DeviceAdmin(admin.ModelAdmin): 
    list_display = ['name','slug']
    list_editable = ['slug']
    
    #list_filter = ['name','slug']



admin.site.register(Profile)
admin.site.register(ACategory)
admin.site.register(Trendy_Products)
admin.site.register(Customer)
admin.site.register(OrderItem)
admin.site.register(ShippngAddress)
admin.site.register(Order)
 
 
