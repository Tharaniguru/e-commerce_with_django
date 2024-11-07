from ecomapp import views
from django.urls import path

urlpatterns = [
    path('',views.getRoutes,name="getRoutes"),
    path('products/',views.getProducts,name="getproducts"),
    path('product/<str:pk>',views.getProduct,name="getproduct"),

]
