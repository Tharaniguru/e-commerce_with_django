from ecomapp import views
from django.urls import path

urlpatterns = [
    path('',views.getRoutes,name="getRoutes"),
    path('product/',views.getProduct,name="getproducts"),
]
