from django.contrib import admin
from store import models

# Register your models here.

admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.Image)
admin.site.register(models.Size)
admin.site.register(models.Inventory)
admin.site.register(models.Item)
admin.site.register(models.Order)