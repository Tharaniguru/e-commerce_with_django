from django.contrib import admin
from .models import *

# Register your models here.

# class CategoryAdmin(admin.ModelAdmin):
#   list_display = ('name', 'image', 'description')
# admin.site.register(Catagory,CategoryAdmin)
admin.site.register(Catagory)
admin.site.register(Product)
admin.site.register(Subcatagory)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'phone_number', 'email']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'payment_date', 'payment_id']
