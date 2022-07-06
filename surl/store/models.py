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
    description = models.TextField(null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Image(models.Model):
    def directory_path(instance, filename):
        return 'store/images/{0}/{1}/{2}'.format(instance.product.category, instance.product.name, filename)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=directory_path)

    def __str__(self):
        return str(self.image)


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
    phone_no = models.CharField(max_length=14)
    email_ad = models.EmailField(max_length=255)
    shipping_ad = models.CharField(max_length=500)
    billing_ad = models.CharField(max_length=500)
    date_of_purchase = models.DateTimeField(default=timezone.now)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length= 1, choices=STATUS, default='P')

    def __str__(self):
        return self.guest_name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    item = models.ForeignKey(Inventory, on_delete=models.PROTECT)


class Notify(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return '{0} - {1}'.format(self.product, self.email)