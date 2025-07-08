from django.db import models
from products.models import Product, PaperType, Size

class Order(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Chưa thanh toán'),
        ('paid', 'Đã thanh toán'),
    ]

    order_code = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.order_code

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    paper_type = models.ForeignKey(PaperType, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    file_upload = models.FileField(upload_to='order_files/', blank=True, null=True)

    def __str__(self):
        return f"{self.order.order_code} - {self.product.name}"
