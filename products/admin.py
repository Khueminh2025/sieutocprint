from django.contrib import admin
from .models import Product, PaperType, Size, PriceTier

admin.site.register(Product)
admin.site.register(PaperType)
admin.site.register(Size)
admin.site.register(PriceTier)
