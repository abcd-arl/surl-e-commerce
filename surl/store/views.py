from django.shortcuts import render
from django.http import HttpResponse
from . import models

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def index(response):
    return HttpResponse('hello')


def product(response, id):
    product = models.Product.objects.get(id=id)
    return HttpResponse(product)