from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from store.api.serializers import ProductAllSerializer, ProductSerializer, InventorySerializer, NotifySerializer, OrderSerializer, OrderItemSerializer
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


@api_view(['POST'])
def api_notify(request):
    serializer = NotifySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def api_purchase(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def api_add_purchase_item(request):
    serializer = OrderItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        item = models.Inventory.objects.get(id=serializer.data['item'])
        item.stocks = item.stocks - 1
        item.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


    # if request.method == 'PUT':
    #     try:
    #         inventory = models.Inventory.objects.get(id=id)
    #     except:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    #     serializer = InventorySerializer(inventory, data=request.data)
    #     data = {}
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    # return Response(status=status.HTTP_400_BAD_REQUEST)