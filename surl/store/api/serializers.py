
from rest_framework import serializers
from store import models


class ImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Image
        fields = ['image']


class InventorySerializer(serializers.ModelSerializer):

    images = serializers.SerializerMethodField()
    product_id = serializers.ReadOnlyField(source='product.id')
    product = serializers.ReadOnlyField(source='product.name')
    size = serializers.ReadOnlyField(source='size.name')

    def get_images(self, obj):
        img = models.Image.objects.filter(product=obj.id)
        return ImageSerializer(img, many=True).data


    class Meta:
        model = models.Inventory
        fields = ['product_id', 'product', 'size', 'stocks', 'images']

        
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
    total_stocks = serializers.SerializerMethodField()

    def get_images(self, obj):
        # images = []
        # all_images = models.Image.objects.filter(product=obj.id)
        # for image in all_images:
        #     images.append(image.image.path)
        # return images

        img = models.Image.objects.filter(product=obj.id)
        return ImageSerializer(img, many=True).data


    def get_total_stocks(self, obj):
        total_stocks = 0
        product = models.Inventory.objects.filter(product=obj.id)
        for p in product:
            total_stocks = total_stocks + p.stocks

        return total_stocks


    class Meta:
        model = models.Product
        fields = ['id', 'name', 'price', 'description','total_stocks', 'images', 'date_created', ]


