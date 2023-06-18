from django.contrib.auth.models import User
# from app.forms import *
# ##Start Hp EDITS
# Create your views here.

from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect, get_object_or_404 
from app.models import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required 
from app.forms import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.http import JsonResponse
import re
import json
##Start Hp EDITS
 
##End Hp EDITS


cont ={}
 
 
'''
def register_tager(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
             
            instance.save()
            return redirect('login')
        else:
            form = RegisterUserForm(request.POST)
    cont['title'] = "التسجيل"
    cont['form'] = form
    return render(request,'accounts/logout.html',cont)
    '''
# Create your views here.
@login_required(login_url='login')

def profil(request,id):
        
        
    profil =  get_object_or_404(Profile,id=id)
    user =  get_object_or_404(User,id=id)
    
    context = {
        'profil': profil,
        'user':user
    }
    return render(request,'profile/profil.html',context)
#@login_required(login_url='login')
@csrf_exempt
def index(request):
    order = None
    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.filter(customer=customer, complete=False).first()
        if not order:
            order = Order.objects.create(customer=customer, complete=False)
        items = order.orderitem_set.all() if order is not None else []
        #cartItems = order.get_cart_items() if order is not None else 0
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = 0
    home = Trendy_Products.objects.all()
    categories = ACategory.objects.all().order_by('name')
    context = {
        'Category': categories,
        'home': home,
        #'cartItems': cartItems
    }
    return render(request, 'home.html', context)
@login_required(login_url='login')

def shop(request):
    home = Trendy_Products.objects.all()
    categories = ACategory.objects.all().order_by('name')
    name = None
    if 'search_name' in request.GET:
        name = request.GET['search_name']
        if name:
            home = home.filter(name__icontains=name)
    context = {
        'index': home,
        'Category': categories.order_by('name'),
    }
    return render(request, 'shop\shop.html', context)
  
  
 

def details_product(request ,slug):
    detailss = get_object_or_404(Trendy_Products,slug = slug)
    
    context = {
   
         'detailss': detailss,
        }
    
    
    return render (request,'shop\details_product.html',context)
@csrf_exempt
def logi(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user =auth.authenticate(username=username,password=password)
        
        if user is not None:
     
             auth.login(request, user)
             messages.success(request, 'You are now logged in')
             
             
             return redirect('index')
        else:
            messages.info(request, 'The Password or username is incorrect')
            
            return redirect('login')
        
        
    
    return render (request,'accounts\login.html')
   
  
def search(request):
    return render (request,'search.html')



def cart(request ):
    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.filter(customer=customer, complete=False).first()
        if not order:
            order = Order.objects.create(customer=customer, complete=False)
        items = order.orderitem_set.all()
            
        #cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        #cartItems =order['get_cart_items']
       
    context = {'items': items, 'order': order}
    
    return render (request,'shop\cart.html',context)
 
@csrf_exempt
def register(request ):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        profilform = NewProfileForm(request.POST)
         
        if form.is_valid():
             
            user = form.save()
            profilform.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    profilform = NewProfileForm
    return render (request=request, template_name='accounts/registrati.html', context={"register_form":form,"profilform":profilform})
   
        #if request.method=='POST':
         #  
          #      first_name = request.POST.get('first_name')
           #     email= request.POST.get('email_address ')
            #    password = request.POST.get('password')
             #   username = request.POST.get('username')
                 
                
              #  user = User.objects.create_user(first_name=first_name,password=password,email=email,username=username)
               # user.save() ##  هو بيعمل يوزر بس و لسا مش بيعمله لوجن
              
                #print(email)
                #print(first_name)
                
                
        ##End Hp EDITS

                #return render (request,'home.html')
            
        #else:
         #  return render (request,'accounts/registrati.html')
def logou (request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect ('index')
def confirmation(request):

    return render(request,'shop/confirmation.html')
@csrf_exempt

 
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action: ',action)
    print('Product: ',productId)
    customer = request.user.customer
    product = Trendy_Products.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem ,created = OrderItem.objects.get_or_create(order=order ,product=product)
    if action == 'add':
        orderItem.quantity=(orderItem.quantity + 1)
    elif action =='remove':
       orderItem.quantity=(orderItem.quantity - 0)
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    
    
    return JsonResponse('Item was added ',safe=False)
 