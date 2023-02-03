from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=120,blank=True,null=True)
    price = models.FloatField(blank=True,null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_create = models.DateField(blank=True,null=True)
    model_prod = models.CharField(max_length=30,blank=True,null=True)
    image = models.ImageField(upload_to="product")
    
    def __str__(self):
        return self.name