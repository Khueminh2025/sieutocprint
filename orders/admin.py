from django.contrib import admin
from .models import Order, OrderItem

# admin.site.register(Order)
# admin.site.register(OrderItem)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_code', 'customer_name', 'phone_number', 'payment_status', 'created_at')
    list_filter = ('payment_status', 'created_at')
    search_fields = ('order_code', 'customer_name', 'phone_number')
    inlines = [OrderItemInline]
    list_editable = ('payment_status',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')