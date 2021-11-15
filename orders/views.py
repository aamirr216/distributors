from django.contrib.auth.models import User
from django.shortcuts import render, redirect,get_object_or_404
from products.models import Shop, Order, Product, Supplier
from django.contrib.auth.decorators import login_required
from django.contrib import messages,auth


# Create your views here.
@login_required(login_url='login')
def index(request):
    qtycount = 10000
    shops = Shop.objects.all().order_by('shopname')
    products = Product.objects.all().order_by('id')
    context = {
        'shops': shops,
        'products': products,
    }
    return render(request, 'orders/index.html',context)

def ordercreate(request):
    shopid = request.POST['shop']
    empid = request.user.id
    # for prod in request.POST.getlist('products'):    
    for prod, qty in zip(request.POST.getlist('products'), request.POST.getlist('qty')):
        orders = Order(product_id=prod,qty=qty,shop_id=shopid,emp_id=empid)
        orders.save()
    return redirect('orders')  

def orderlist(request, shop_id):
    empid = request.user.id
    print('orderlist')
    # shop_id = get_object_or_404(Shop, pk=shop_id)
    if empid!=1:
        shop = Shop.objects.get(id=shop_id)   
        orders=Order.objects.raw('SELECT o.id, o.product_id, o.shop_id, p.product_name,o.qty,o.date from products_order o JOIN products_product p ON o.product_id = p.id JOIN products_shop s ON o.shop_id = s.id JOIN products_delivery d ON d.order_id <> o.id AND o.emp_id=%s',[empid])
         
        # orders = Order.objects.filter(shop_id=shop_id,emp_id=empid).prefetch_related('product__order_set')
    else:
        shop = Shop.objects.get(id=shop_id)    
        orders=Order.objects.raw('SELECT o.id, o.product_id, o.shop_id, p.product_name,o.qty,o.date from products_order o JOIN products_product p ON o.product_id = p.id JOIN products_shop s ON o.shop_id = s.id JOIN products_delivery d ON d.order_id <> o.id')

        
        
    context = {
        'orders': orders
    }
    return render(request, 'orders/orderlist.html',context) 

def order(request, order_id):
    order = Order.objects.get(id=order_id)
    shop_id = order.shop_id
    shop = Shop.objects.get(id=shop_id)
    context = {
        'order': order,
        'shop': shop
    }
    return render(request, 'orders/order.html',context)     

def orderdelete(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            order = request.POST['orderid'] 
            order = Order.objects.filter(id=order)
            order.delete()
            messages.success(request,'Order deleted') 
        else:
            messages.error(request, 'Order not selected')
    else:
        messages.error(request, 'You not Logged in')    
    return redirect('delivery') 

# EDIT ORDER
def orderforedit(request, order_id):
    order = Order.objects.get(id=order_id)
    shop_id = order.shop_id
    shop = Shop.objects.get(id=shop_id)
    context = {
        'order': order,
        'shop': shop
    }
    return render(request, 'orders/orderedit.html',context)   

def orderupdate(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            orderid = request.POST['orderid'] 
            order = Order.objects.get(id=orderid)
            newqty = request.POST['qty']
            order.qty= newqty
            order.save()
            messages.success(request,'Order Updated') 
        else:
            messages.error(request, 'Order not selected')
    else:
        messages.error(request, 'You are not Logged in')    
    return redirect('delivery')  