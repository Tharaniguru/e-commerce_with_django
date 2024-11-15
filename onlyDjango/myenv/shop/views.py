from django.http import  JsonResponse
from django.shortcuts import redirect, render
from shop.form import *
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import json
from django.shortcuts import render, redirect
from .models import UserPreferences, Product


def index(request):
    products=Product.objects.filter(trending=1)
    return render(request,"shop/index.html",{"products":products})


def collections(request):
  catagory=Catagory.objects.filter(status=0)
  return render(request,"shop/collections.html",{"catagory":catagory})


def logout_page(request):
  if request.user.is_authenticated:
    logout(request)
    messages.success(request,"Logged out Successfully")
  return redirect("login")



def login_page(request):
  if request.user.is_authenticated:
    return redirect("home")
  else:
    if request.method=='POST':
      name=request.POST.get('username')
      pwd=request.POST.get('password')
      user=authenticate(request,username=name,password=pwd)
      if user is not None:
        login(request,user)
        messages.success(request,"Logged in Successfully")
        return redirect("home")
      else:
        messages.error(request,"Invalid User Name or Password")
        return redirect("/login")
    return render(request,"shop/login.html")


def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success You can Login Now..!")
            return redirect('/login')
    return render(request,"shop/register.html",{'form':form})

def collectionsview(request, name):
    if Catagory.objects.filter(name=name, status=0).exists():
        subcatagory = Subcatagory.objects.filter(category__name=name)
        return render(request, "shop/subcategory/index.html", {"subcatagory": subcatagory, "subcatagory_name": name})
    else:
        messages.warning(request, "No Such Category Found")
        return redirect('collections')

  
def product(request, name):
    if Subcatagory.objects.filter(name=name, status=0):
        products = Product.objects.filter(subcategory__name=name, status=0)
        return render(request, "shop/product/index.html", {"products": products, "subcategory_name": name})

    else:
        messages.warning(request, "No such Subcategory Found")
        return redirect('collections')

def product_details(request, cname, pname):
    if Subcatagory.objects.filter(name=cname, status=0).exists():
        if Product.objects.filter(name=pname, status=0).exists():
            product = Product.objects.filter(name=pname, status=0).first()
            
            # Fetch five related products from the same subcategory (excluding the current product)
            related_products = Product.objects.filter(subcategory=product.subcategory, status=0).exclude(name=pname)[:5]
            
            # Pass related_products to the template
            return render(request, "shop/product/product_details.html", {
                "product": product,
                "subcategory_name": cname,
                "related_products": related_products
            })
        else:
            messages.error(request, "No Such Product Found")
            return redirect('collections')
    else:
        messages.error(request, "No Such Category Found")
        return redirect('collections')


def favviewpage(request):
  if request.user.is_authenticated:
    fav=Favourite.objects.filter(user=request.user)
    return render(request,"shop/fav.html",{"fav":fav})
  else:
    return redirect("/")
 
def remove_fav(request,fid):
  item=Favourite.objects.get(id=fid)
  item.delete()
  return redirect("/favviewpage")
 

def cart_page(request):
  if request.user.is_authenticated:
    cart=Cart.objects.filter(user=request.user)
    return render(request,"shop/cart.html",{"cart":cart})
  else:
    return redirect("/")
 
def remove_cart(request,cid):
  cartitem=Cart.objects.get(id=cid)
  cartitem.delete()
  return redirect("/cart")
 

def fav_page(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      product_id=data['pid']
      product_status=Product.objects.get(id=product_id)
      if product_status:
         if Favourite.objects.filter(user=request.user.id,product_id=product_id):
          return JsonResponse({'status':'Product Already in Favourite'}, status=200)
         else:
          Favourite.objects.create(user=request.user,product_id=product_id)
          return JsonResponse({'status':'Product Added to Favourite'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Favourite'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)
 
 
def add_to_cart(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      product_qty=data['product_qty']
      product_id=data['pid']
      #print(request.user.id)
      product_status=Product.objects.get(id=product_id)
      if product_status:
        if Cart.objects.filter(user=request.user.id,product_id=product_id):
          return JsonResponse({'status':'Product Already in Cart'}, status=200)
        else:
          if product_status.quantity>=product_qty:
            Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
            return JsonResponse({'status':'Product Added to Cart'}, status=200)
          else:
            return JsonResponse({'status':'Product Stock Not Available'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Cart'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)
   




def search_results(request):
    query = request.GET.get('query', '')  # Get the search query from the form
    if query:
        # Filter products based on the query
        products = Product.objects.filter(name__icontains=query)  # Assuming your product has a 'name' field
    else:
        products = Product.objects.all()  # Show all products if no search query

    return render(request, 'shop/search_results.html', {'products': products, 'query': query})




def profile_view(request):
    user_preferences, created = UserPreferences.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserPreferencesForm(request.POST, instance=user_preferences)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page or wherever needed
    else:
        form = UserPreferencesForm(instance=user_preferences)

    context = {
        'form': form,
    }
    return render(request, 'shop/profile.html')


def home_view(request):
    # Assume this is your main view where the navbar context is rendered.
    if request.user.is_authenticated:
        try:
            user_preferences = UserPreferences.objects.get(user=request.user)
            selected_products = [
                user_preferences.product_1,
                user_preferences.product_2,
                user_preferences.product_3,
            ]
            selected_products = [product for product in selected_products if product is not None]
        except UserPreferences.DoesNotExist:
            selected_products = []
    else:
        selected_products = []

    context = {
        'related_products': selected_products,
    }
    
    return render(request, 'home.html', context)