from urllib.request import urlopen
import json
from django.shortcuts import render
from django.http import HttpResponse
from . import models

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def index(response):
    return HttpResponse('hello')


def store(response):
    return render(response, 'store/store.html', {})


def product(response, id):
    url = urlopen("http://127.0.0.1:8000/api/product/{}/".format(str(id)))
    
    data = json.loads(url.read())
    print(data)
    return render(response, 'store/product.html', {'id': id})
