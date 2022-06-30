from itertools import product
from pyexpat import model
from unicodedata import name
from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, to_field='name', on_delete=models.CASCADE)
    description = models.CharField(max_length=700, null=True)
    date_created = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/images/{}'.format(product.name))

    def __str__(self):
        return "self.image"


class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, blank=True)
    stocks = models.PositiveIntegerField()

    class Meta:
        unique_together = ('product', 'size',)

    def __str__(self):
        return "{} - {}".format(self.product, self.size)


class Order(models.Model):

    STATUS = (
        ('P', 'PENDING'),
        ('A', 'ACCEPTED'),
        ('R', 'REJECTED'),
        ('S', 'SUCCESSFUL'),
        ('F', 'FAILED')
    )

    guest_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=13)
    email_ad = models.EmailField(max_length=255)
    shipping_ad = models.CharField(max_length=255)
    billing_ad = models.CharField(max_length=255)
    date_of_purchase = models.DateField()
    total = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length= 1, choices=STATUS, default='P')

    def __str__(self):
        return self.guest_name


class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    item = models.ForeignKey(Inventory, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=6, decimal_places=2)
    