from django.contrib import admin
from .models import Shop, Order, Book, Author, Membership, Person, Group, Product, Supplier
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','shop','product','qty')
    list_display_links=('id','product')
    search_fields = ('product', 'shop')
    

# admin.site.register(Order, OrderAdmin)

# class ShopAdmin(admin.ModelAdmin):
#     list_display = ('id','shopname','owner','contactno')
#     list_display_links=('id','shopname')
#     list_filter=('owner','shopname')
#     search_fields = ('shopname', 'owner')

# admin.site.register(Shop, ShopAdmin)

class OrderInline(admin.TabularInline):
    model = Order
    extra = 1

class ShopAdmin(admin.ModelAdmin):
    inlines = (OrderInline,)

admin.site.register(Order, OrderAdmin)
admin.site.register(Shop, ShopAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','product_name','comp_price','price', 'qty','supplier')
    list_display_links=('id','product_name')
    search_fields = ('product_name', 'supplier')

admin.site.register(Product, ProductAdmin)

class SupplierAdmin(admin.ModelAdmin):
    list_display =('id','sup_name','contactperson','contactno', 'location')
    list_display_links=('id','sup_name')
    search_fields = ('sup_name', 'contactperson')
    
admin.site.register(Supplier, SupplierAdmin)

