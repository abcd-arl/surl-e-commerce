from pyexpat import model
from rest_framework import serializers
from store import models

class OrderItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = '__all__'

class NotifySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Notify
        fields = ['product', 'email']

class ImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Image
        fields = ['image']


class InventorySerializer(serializers.ModelSerializer):

    images = serializers.SerializerMethodField()
    product_id = serializers.ReadOnlyField(source='product.id')
    product = serializers.ReadOnlyField(source='product.name')
    price = serializers.ReadOnlyField(source='product.price')
    size = serializers.ReadOnlyField(source='size.name')

    def get_images(self, obj):
        img = models.Image.objects.filter(product=obj.product).first()
        return ImageSerializer(img).data


    class Meta:
        model = models.Inventory
        fields = ['id', 'product_id', 'product', 'size', 'price', 'stocks', 'images']


        
class ProductSerializer(serializers.ModelSerializer):

    images = serializers.SerializerMethodField()
    stocks = serializers.SerializerMethodField()
    total_stocks = serializers.SerializerMethodField()

    def get_images(self, obj):
        img = models.Image.objects.filter(product=obj.id)
        return ImageSerializer(img, many=True).data

    def get_stocks(self, obj):
        s = {}
        product = models.Inventory.objects.filter(product=obj.id)
        for p in product:
            s[p.size.name] = p.stocks

        return s

    def get_total_stocks(self, obj):
        total_stocks = 0
        product = models.Inventory.objects.filter(product=obj.id)
        for p in product:
            total_stocks = total_stocks + p.stocks

        return total_stocks

    class Meta:
        model = models.Product
        fields = ['id', 'name', 'price', 'description', 'images', 'total_stocks', 'stocks', 'date_created', ]


class ProductAllSerializer(serializers.ModelSerializer):

    images = serializers.SerializerMethodField()
    stocks = serializers.SerializerMethodField()
    total_stocks = serializers.SerializerMethodField()

    def get_images(self, obj):
        img = models.Image.objects.filter(product=obj.id)
        return ImageSerializer(img, many=True).data

    def get_stocks(self, obj):
        s = {}
        product = models.Inventory.objects.filter(product=obj.id)
        for p in product:
            s[p.size.name] = p.stocks

        return s

    def get_total_stocks(self, obj):
        total_stocks = 0
        product = models.Inventory.objects.filter(product=obj.id)
        for p in product:
            total_stocks = total_stocks + p.stocks

        return total_stocks


    class Meta:
        model = models.Product
        fields = ['id', 'name', 'price', 'description','total_stocks', 'stocks', 'images', 'date_created', ]


