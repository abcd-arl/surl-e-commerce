from itertools import product
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http import JsonResponse

from store.api.serializers import ProductAllSerializer, ProductSerializer, InventorySerializer
from store import models

@api_view(['GET'])
def api_store(request, category):
    try:
        if category != 'All':
            products = models.Product.objects.filter(category=category).order_by('-date_created')
        else:
            products = models.Product.objects.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProductAllSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_product(request, id):
    try:
        product = models.Product.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
def api_inventory(request):
    try:
        inventory = models.Inventory.objects.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = InventorySerializer(inventory, many=True)
    return Response(serializer.data)