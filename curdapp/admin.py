from django.contrib import admin
from .models import  ProductData
class AdminProductData(admin.ModelAdmin):
    list_display = ['product_number','product_name','product_class','product_weight']
admin.site.register(ProductData,AdminProductData)
