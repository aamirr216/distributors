from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from products.models import Delivery, Shop, Order, Product, Supplier, Delivery

@login_required(login_url='login')
def index(request):
    empid = request.user.id
    # orders = Order.objects.all().prefetch_related('product__order_set')
    if empid!=1:
        orderscount = Order.objects.filter(emp_id=empid).count()
        orderdelivered = Delivery.objects.filter(emp_id=empid).count()
        orderscount=orderscount-orderdelivered
    else:
        orderscount = Order.objects.all().count()
        orderdelivered = Delivery.objects.all().count()
        orderscount=orderscount-orderdelivered
        
    # orderscount = Order.objects.filter(emp_id=empid).select_related().defer('order__delivery').count()
    
    context = {
        'orderscount': orderscount      
    }
    return render(request, 'pages/index.html',context)     
    # return render(request, 'pages/index.html')

@login_required(login_url='login')
def about(request):
    return render(request, 'pages/about.html')

def orderlist(request, shop_id):
    orders = Order.objects.all().prefetch_related('product__order_set')
    context = {
        'orders': orders      
    }
    return render(request, 'pages/index.html',context)  