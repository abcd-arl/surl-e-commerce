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
    return render(response, 'store/product.html', {'id': id})


def bag(response):
    return render(response, 'store/bag.html', {})


def checkout(response):
    return render(response, 'store/checkout.html', {})


def thankyou(response, id):
    return render(response, 'store/thank-you-for-shopping.html', {'id': id})


def ongoing(response):
    return render(response, 'store/ongoing.html', {})
    