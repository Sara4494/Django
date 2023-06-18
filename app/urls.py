from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('products/',views.list_prod, name='list_prod'),
    path('product/',views.product_form , name="product_form"),
    path('elmagmo3a/',views.elmago ,name="function_elmgmo3a"),
    path('prod/<str:slug>/',views.get_product,name="product_detail"),
    #  {% url 'name_in_url' elmot8ayer %}
    
]


