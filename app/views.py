from django.shortcuts import render
from app.models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def list_prod(request):
    
    all_product = Product.objects.all()
    el_context = {
        'all_prod':all_product
    }
    return render(request,'product/all_prod.html',el_context)