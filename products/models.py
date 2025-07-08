from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='product_images/', blank=True)

    def __str__(self):
        return self.name

class PaperType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=50)  # Ví dụ: A4, 9x5cm

    def __str__(self):
        return self.name

class PriceTier(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    paper_type = models.ForeignKey(PaperType, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('product', 'paper_type', 'size', 'quantity')

    def __str__(self):
        return f"{self.product.name} - {self.paper_type.name} - {self.size.name} - SL: {self.quantity}"
