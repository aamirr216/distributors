from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='orders'),
    path('ordercreate', views.ordercreate, name="ordercreate"),
    path('<int:shop_id>', views.orderlist, name='orderlist'), 
    path('order/<int:order_id>', views.order, name='order'),
    path('orderforedit/<int:order_id>', views.orderforedit, name='orderforedit'),
    path('orderdelete', views.orderdelete, name="orderdelete"),
    path('orderupdate', views.orderupdate, name="orderupdate"),   

]