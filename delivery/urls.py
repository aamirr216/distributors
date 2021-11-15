from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='delivery'),
    path('<int:shop_id>', views.fordeliver, name='fordeliver'), 
    path('deliverorders', views.deliverorders, name='deliverorders'),   
    path('delivered_list', views.delivered_list, name='delivered_list'),   
        
    # path('ordercreate', views.ordercreate, name="ordercreate"),
    # path('products', views.products, name='products'),
    # path('', views.products, name='products'),    
]