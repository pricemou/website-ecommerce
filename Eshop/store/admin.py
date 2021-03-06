from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer

# Creation d'une class
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category','image']
    
class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone','email','password']

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer,AdminCustomer)