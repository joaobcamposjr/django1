from django.contrib import admin
from .models import Product, Client


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'email')


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)