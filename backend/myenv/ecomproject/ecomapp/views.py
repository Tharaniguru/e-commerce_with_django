from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from .products import products
from .models import Products
from .serializer import ProductSerializer


@api_view(['GET'])
def getRoutes(request):
    return Response("hello")

@api_view(['GET'])
def getProducts(request):
    products =Products.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def getProduct(request,pk):
    product=Products.objects.get(_id=pk)
    serializer=ProductSerializer(product,many=False)
    return Response(serializer.data)
    