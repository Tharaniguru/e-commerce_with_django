from django.contrib import admin
from .models import *

# Register your models here.

# class CategoryAdmin(admin.ModelAdmin):
#   list_display = ('name', 'image', 'description')
# admin.site.register(Catagory,CategoryAdmin)
admin.site.register(Catagory)
admin.site.register(Product)
admin.site.register(Subcatagory)
