from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE ,null=True ,blank=True )
    name = models.CharField(max_length=200, null=True  )
    email = models.CharField(max_length=200, null=True  )
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True ,blank=True)

     
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
 
    
class Product(models.Model):
    name = models.CharField(max_length=50, null=True  )
    price = models.DecimalField(max_digits= 6 , decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, blank=True, null=True)
    digital =models.BooleanField(default=False, null=True ,blank=True )
    img = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.name
    @property
    def imageURL(self):
        try:
            url =self.img.url
        except:
            url =''
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, blank=True, null=True)
    
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True )
    transaction_id = models.CharField(max_length=200, null=True )
    def __str__(self):
        return str(self.id)
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True

        return  shipping
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
      product = models.ForeignKey(Product,on_delete=models.SET_NULL , null=True)
      order = models.ForeignKey(Order,on_delete=models.SET_NULL, null=True)
      quantity = models.IntegerField(default=0 ,blank=True, null=True)
      date_added = models.DateTimeField(auto_now_add=True)
      @property
      def get_total(self):
        total = self.product.price * self.quantity
        return total
class ShippngAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, blank=True, null=True)
  
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length= 50 ,   null= True)
    phone = models.CharField(max_length=50  , null= True)
    street_name = models.CharField(max_length=50,   null= True)
    building_number = models.CharField(max_length=50,   null= True)
    district = models.CharField(max_length=50 ,  null= True)
  
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


    
     
     
    