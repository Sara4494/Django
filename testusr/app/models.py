from django.db import models

# Create your models here.from django.db import models
from datetime import datetime
from django.utils.text import slugify
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
 
import sys

class Profile(models.Model):
    pos_site = (
        ('admin','Admin'),
        ('Customer','Customer'),
        ('Tager','Tager'),
        )
    ### لازم تفهمى انك تقدرى تدخلى على البروفايل من الريكوست اللى فيها ال user
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    phone_number = models.CharField(max_length=11,verbose_name="Phone number",null=True )
    phone_number2 = models.CharField(max_length=11,verbose_name="Phone number2",null=True , blank=True)
    image = models.ImageField(upload_to="photo/",verbose_name="Profile photos",blank=True, null=True)
    pos_in_store = models.CharField(max_length=50 ,choices=pos_site,verbose_name="صفته بالموقع", blank=True, null=True)
    slug = models.SlugField(("Slug"),blank=True,null=True)
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.user)
        super(Profile,self).save(*args,**kwargs)
    
    def __str__(self):
        return str(self.user)
      
      
      
#@receiver(post_save,sender=User)



class ACategory(models.Model):
    name = models.CharField(max_length=200, db_index=True ,blank= True)
    slug = models.SlugField(max_length=200, unique=True ,blank=True)

     
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
 
class Trendy_Products(models.Model):
       
    Size = (
        ('s','s'),
        ('m','m'),
        ('l','l'),
        ('xl','xl'),
    )
    categor = models.ForeignKey(ACategory, blank=True,null=True, related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=50 ,blank=True ,null= True)
  
    price = models.DecimalField(max_digits= 6 , decimal_places=2)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')#upload_to='photos/%Y/%m/%d/'   عمل فولدر لي الصور بي التاريخ والوقت
    photo2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)   
    photo3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo4 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo5 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo6 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo7 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
 
    details = models.TextField( max_length=1000,null=True,blank=True)
    colors = models.CharField(max_length=20 , blank=True ,null= True)
    size = models.CharField(max_length=10,choices=Size ,null=True,blank=True)
    publish_dete = models.DateTimeField(default=datetime.now)
    
    slug = models.SlugField(("Slug"),blank=True,null=True)
    digital =models.BooleanField(default=False, null=True ,blank=True )

    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Trendy_Products,self).save(*args,**kwargs)

    def __str__(self):
        return self.name
     
     
     
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE ,null=True ,blank=True )
    name = models.CharField(max_length=200, null=True  )
    email = models.CharField(max_length=200, null=True  )
    def __str__(self):
        return self.name
 
    
class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True )
    transaction_id = models.CharField(max_length=200, null=True )
    def __str__(self):
        return str(self.id)
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
      product = models.ForeignKey(Trendy_Products,on_delete=models.SET_NULL , null=True)
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
    address = models.CharField(max_length=50  , null= True)
    city = models.CharField(max_length=50,   null= True)
    zipcode = models.CharField(max_length=50,   null= True)
    state = models.CharField(max_length=50 ,  null= True)
    email = models.CharField(max_length=255,   null= True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
