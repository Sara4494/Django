from django.shortcuts import render , redirect , get_object_or_404
#from django.contrib.auth.decorators import login_required
from app.models import *
from .forms import *

# Create your views here.

def index(request):
    
    print("Indexxxxxxxxxxxxxxxxx")
    return render(request,'index.html')

### CRUD ###
# Create
# Read
# Update
# Delete

def list_prod(request):
    #all_magmo3at = Elmagmo3a.objects.all()
    all_product = Product.objects.all()
    for item in all_product:
        item.name
        item.magmo3a
        item.price
        item.tag
    print(len(all_product))
    print(all_product[0])
    print(type(all_product[0]))
    el_context = {
        'all_prod':all_product
    }
    return render(request,'product/all_prod.html',el_context)

def get_product(request,slug):
    product = get_object_or_404(Product,slug=slug)
    
    context = {
        'product':product,
    }
    return render(request,'product/product_detail.html',context)

def t2oly_3dad_elmotg():
    pass

def product_form(eltalb):
    all_product = Product.objects.all()
    form = ProductForm()
    form2 = ProductForm2()
    if eltalb.method == "POST":
        print("POST")
        form = ProductForm(eltalb.POST) #form = ProuctForm(name=eltalb.POST.get('name')# price=eltalb.POST.get('price'))
        form_instance = form.save(commit=False)
        ## instance = htmlنسخة من الفورم = اقدر اضيف بيانات للفورم خارج ال htm
        ##### الداتا بيز لسة مفيش حاجة اتحفظت فيها
        ### عشان ال commit = False
        form_instance.count = 1
        if form.is_valid():
            form_instance.active = False
            form.save()
            return redirect('list_prod')
        else:
            print("NOT Valid ###############")
            form = ProductForm()
        
    el_context = {
        'form':form,
        'form2':form2,
        'all_prod':all_product
    }
    return render(eltalb,'product/product.html',el_context)

def elmago(request):
    form = Elmamo3aForm()
    if request.method == "POST":
        print("POST")
        form = Elmamo3aForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('list_prod')
        else:
            print("NOT Valid ###############")
            form = Elmamo3aForm()
        
    el_context = {
        'form':form,
    }
    return render(request,'category/elmagmo3a.html',el_context)
