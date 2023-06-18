from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
# Create your views here.
def store(request):
  

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)                                                                                                                                                                                                                                                                                                             
        if not order:
            order = Order.objects.create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0 ,'shipping': False}
        cartItems =order['get_cart_items']
    products = Product.objects.all()
    categories = Category.objects.all().order_by('name')
    
    context = {'items': items, 'order': order,  'cartItems':cartItems,'products':products ,'Category':categories}
    
    
    return render(request, 'store.html', context)

         
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.filter(customer=customer, complete=False).first()
        if not order:
            order = Order.objects.create(customer=customer, complete=False)
        items = order.orderitem_set.all()
            
        cartItems = order.get_cart_items
        products = Product.objects.all()
        categories = Category.objects.all().order_by('name')

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0,'shipping': False}
        cartItems =order['get_cart_items']
       
    context = {'items': items, 'order': order ,  'cartItems':cartItems ,'Category':categories}
    
   
    
    return render(request, 'cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order_tuple = Order.objects.get_or_create(customer=customer, complete=False)
        order = order_tuple[0]  # get the first element of the tuple
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        
        # Store the order variable in the session
        request.session['order'] = {
            'id': order.id,
            'cartItems': cartItems,
            'complete': order.complete,
        }

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0,'shipping': False}
        cartItems = order['get_cart_items']
        
        # Store the order variable in the session
        request.session['order'] = {
            'id': None,
            'cartItems': cartItems,
            'complete': False,
        }

    context = {'items': items , 'order' : order , 'cartItems' : cartItems}
    return render(request, 'checkout.html',context)

 
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action: ',action)
    print('Product: ',productId)
    custmer = request.user.customer

    product = Product.objects.get(id=productId)
    order ,created = Order.objects.get_or_create(customer=custmer, complete=False)
    orderItem ,created = OrderItem.objects.get_or_create(order=order ,product=product)


    
    if action == 'add':
        orderItem.quantity = orderItem.quantity + 1
    elif action == 'remove':
        orderItem.quantity = orderItem.quantity - 1
    
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse('Item was added', safe=False)
 