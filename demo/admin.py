from django.contrib import admin

from demo.models import Category, Product, Media

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Media)