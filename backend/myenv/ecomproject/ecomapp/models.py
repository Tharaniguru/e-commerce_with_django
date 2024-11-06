from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Products(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    productname=models.CharField(max_length=150)
    image=models.ImageField(null=True,blank=True)
    productbrand=models.CharField(max_length=150,null=True,blank=True)
    productcategory=models.CharField(max_length=150,null=True,blank=True)
    productinfo=models.TextField(null=True,blank=True)
    rating=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    stockcount=models.IntegerField(null=True,blank=True,default=0)
    createdat=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)


    def __str__(self): 
        return self.productname