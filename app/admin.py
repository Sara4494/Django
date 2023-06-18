from django.contrib import admin
from app.models import *

# Register your models here.

class ProductAdminCustomize(admin.ModelAdmin):
    search_fields = ['name','model_prod']
    list_display = ['name','price','active','magmo3a']
    list_editable = ['price','magmo3a','active']
    list_filter = ['date_added','active']
    list_per_page = 20
    
    
class magmo3aAdminCustomize(admin.ModelAdmin):
    list_display = ['name','type_magmo3a']
    
admin.site.register(Product,ProductAdminCustomize)
admin.site.register(Elmagmo3a,magmo3aAdminCustomize)
admin.site.register(Tag)
admin.site.register(Profile)
