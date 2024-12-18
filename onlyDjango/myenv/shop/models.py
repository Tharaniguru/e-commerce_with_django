from django.db import models
import datetime
import os
from django.contrib.auth.models import User


def getFileName(requset,filename):
  now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
  new_filename="%s%s"%(now_time,filename)
  return os.path.join('uploads/',new_filename)


class Catagory(models.Model):
  name=models.CharField(max_length=150,null=False,blank=False)
  image=models.ImageField(upload_to=getFileName,null=True,blank=True)
  description=models.TextField(max_length=500,null=False,blank=False)
  status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
  created_at=models.DateTimeField(auto_now_add=True)
  trending = models.BooleanField(default=False,help_text="0-default,1-Trending")
 
  def __str__(self) :
    return self.name
  
class Subcatagory(models.Model):
  category=models.ForeignKey(Catagory,on_delete=models.CASCADE)
  name = name=models.CharField(max_length=150,null=False,blank=False)
  status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
  created_at=models.DateTimeField(auto_now_add=True)
  trending = models.BooleanField(default=False,help_text="0-default,1-Trending")
  sub_image=models.ImageField(upload_to=getFileName,null=True,blank=True)

  def __str__(self) :
    return self.name
  
class Product(models.Model):
  subcategory=models.ForeignKey(Subcatagory,on_delete=models.CASCADE,default=1)
  name=models.CharField(max_length=150,null=False,blank=False)
  vendor=models.CharField(max_length=150,null=False,blank=False)
  product_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
  quantity=models.IntegerField(null=False,blank=False)
  original_price=models.FloatField(null=False,blank=False)
  selling_price=models.FloatField(null=False,blank=False)
  description=models.TextField(max_length=500,null=False,blank=False)
  status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
  trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
  created_at=models.DateTimeField(auto_now_add=True)
 
  def __str__(self) :
    return self.name



class Cart(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  product=models.ForeignKey(Product,on_delete=models.CASCADE)
  product_qty=models.IntegerField(null=False,blank=False)
  created_at=models.DateTimeField(auto_now_add=True)
 
  @property
  def total_cost(self):
    return self.product_qty*self.product.selling_price
 
class Favourite(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	created_at=models.DateTimeField(auto_now_add=True)
 


class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product_1 = models.ForeignKey(Product, related_name='product_1', on_delete=models.SET_NULL, null=True, blank=True)
    product_2 = models.ForeignKey(Product, related_name='product_2', on_delete=models.SET_NULL, null=True, blank=True)
    product_3 = models.ForeignKey(Product, related_name='product_3', on_delete=models.SET_NULL, null=True, blank=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)  # Add address field



    def __str__(self):
        return self.user.username

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Payment {self.payment_id} by {self.user.username}"