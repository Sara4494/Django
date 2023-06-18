
from django.urls import path
from app.views import *

urlpatterns = [
    path('',index,name= 'index'),
    path('shop/',shop,name= 'shop'),
    path('details_product/<slug:slug>/',details_product,name= 'details_product'),
    path('cart/',cart,name= 'cart'),
    path('profil/<int:id>/',profil,name= 'profil'),
    path('search/',search,name= 'search'),
    path('registrati/',register,name='registrati'),
    path('login',logi,name='login'),
    path('logout',logou,name='logout'),
    path('confirmation', confirmation, name='confirmation'),
    path('uodate_item/', updateItem, name='updateItem')
     
    
    
]