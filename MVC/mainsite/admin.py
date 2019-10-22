from django.contrib import admin

# Register your models here.

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=('sku','name','price','size','inventory')

admin.site.register(Product,ProductAdmin)