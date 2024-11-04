from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

def getRoutes(request):
    return HttpResponse("hello")
