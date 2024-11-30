from django.urls import path
from . import views
urlpatterns = [
    
    path("", views.index, name="index"),
    path('home/',views.index,name='home'),
    path('login/',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('collections/',views.collections,name='collections'), #catagory
    path('collections/<str:name>',views.collectionsview,name='collectionsview'),#subcatagory
    path('product/<str:name>',views.product,name='product'),#product
    path('product/<str:cname>/<str:pname>',views.product_details,name="product_details"),
    path('register/',views.register,name="register"),
    path('addtocart',views.add_to_cart,name="addtocart"),
    path('cart',views.cart_page,name="cart"),
    path('fav',views.fav_page,name="fav"),
    path('favviewpage',views.favviewpage,name="favviewpage"),
    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),
    path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),
    path('collections',views.collections,name="collections"),
    path('search/', views.search_results, name='search_results'),
    path('payment/', views.payment, name='payment'),


    path('profile/', views.profile_view, name='profile'),
]
