from unicodedata import name
from urllib import request
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
import csv
from .models import Movies 
# Create your views here.

def home(request):
   return render(request,'index.html')

def createDatabase(request):
   if request.method == 'GET':
      name = request.GET.get('name')
      limit = request.GET.get('limit')
      payload = []
      if limit:
         data_ = Movies.objects.filter(name__icontains=name)[:int(limit)]

      else:
         data_ = Movies.objects.filter(name__icontains=name)
      for i in data_:
         payload.append([i.name,i.url])
   return JsonResponse({'status': 200, 'data': payload})