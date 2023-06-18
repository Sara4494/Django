
from django.urls import path 
from app.views import*
urlpatterns = [
     path('cart/', cart, name='cart'),
     path('checkout/' , checkout,name='checkout'),
     path('' ,store ,name='store'),
    path('uodate_item/', updateItem, name='updateItem')

     
]
 