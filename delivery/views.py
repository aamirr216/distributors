from django.contrib.auth.models import User
from django.shortcuts import render, redirect,get_object_or_404
from products.models import Delivery, Shop, Order, Product, Supplier
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def index(request):
    empid = request.user.id
    # shops = Shop.objects.all().order_by('shopname')
    # products = Product.objects.all().order_by('id')
    if empid!=1:
        shops=Order.objects.raw('SELECT DISTINCT(s.id), s.shopname FROM PRODUCTS_SHOP s JOIN PRODUCTS_ORDER o ON o.shop_id=s.id JOIN products_delivery d ON d.order_id<>o.id and o.emp_id=%s',[empid])
    else:
        shops=Order.objects.raw('SELECT DISTINCT(s.id), s.shopname FROM PRODUCTS_SHOP s JOIN PRODUCTS_ORDER o ON o.shop_id=s.id JOIN products_delivery d ON d.order_id<>o.id')
        
    context = {
        'shops': shops
    }
    return render(request, 'delivery/index.html',context)

def fordeliver(request, shop_id):
    empid = request.user.id
    # THIS CODE WORKING ONLY JOIN TABLE WITH EQUAL TWO COLUMN [
    # orders = Order.objects.filter(shop_id=shop_id,emp_id=empid).prefetch_related('product__order_set') 
    # ]
    if empid!=1:    
        orders=Order.objects.raw('SELECT o.id,o.emp_id,o.shop_id,o.product_id, p.product_name,o.date FROM PRODUCTS_ORDER o JOIN PRODUCTS_PRODUCT p ON o.product_id = p.id JOIN PRODUCTS_DELIVERY d ON d.order_id <> o.id AND d.emp_id=%s AND o.shop_id = %s',[empid,shop_id])
    else:
        orders=Order.objects.raw('SELECT o.id,o.emp_id,o.shop_id,o.product_id, p.product_name,o.date FROM PRODUCTS_ORDER o JOIN PRODUCTS_PRODUCT p ON o.product_id = p.id JOIN PRODUCTS_DELIVERY d ON d.order_id <> o.id AND o.shop_id = %s',[shop_id])
        
    context = {
        'orders': orders
    }
    return render(request, 'delivery/fordeliver.html',context)

def delivered_list(request):
    empid = request.user.id
    
    if empid!=1:
        deliveries=Delivery.objects.raw('SELECT d.id, d.order_id,d.qty,d.date,d.emp_id,p.product_name,s.shopname,u.username FROM products_delivery d JOIN products_order o ON o.id = d.order_id and d.emp_id=%s JOIN products_product p ON p.id = o.product_id JOIN products_shop s ON s.id = o.shop_id JOIN auth_user U ON d.emp_id=u.id order by d.id DESC',[empid])
    else:
        deliveries=Delivery.objects.raw('SELECT d.id, d.order_id,d.qty,d.date,d.emp_id,p.product_name,s.shopname,u.username FROM products_delivery d JOIN products_order o ON o.id = d.order_id JOIN products_product p ON p.id = o.product_id JOIN products_shop s ON s.id = o.shop_id JOIN auth_user U ON d.emp_id=u.id order by d.id DESC')
    
    context = {
        'deliveries': deliveries
    }
    return render(request, 'delivery/deliveredlist.html',context)
    
def deliverorders(request):
    empid = request.user.id
    if empid!=1:
        for order, qty in zip(request.POST.getlist('orderid'), request.POST.getlist('qty')):
            delivery = Delivery(qty=qty,order_id=order,emp_id=empid)
            delivery.save()
    else:
        for order, qty in zip(request.POST.getlist('orderid'), request.POST.getlist('qty')):
            delivery = Delivery(qty=qty,order_id=order,emp_id=1)
            delivery.save()
        
    return redirect('orders')  
