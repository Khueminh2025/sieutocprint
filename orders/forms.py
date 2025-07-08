from django import forms
from .models import Order, OrderItem
from products.models import Product, PaperType, Size

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'phone_number', 'email', 'address', 'note']

class OrderItemForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    paper_type = forms.ModelChoiceField(queryset=PaperType.objects.all())
    size = forms.ModelChoiceField(queryset=Size.objects.all())
    quantity = forms.IntegerField(min_value=1)
    file_upload = forms.FileField(required=False)

class OrderLookupForm(forms.Form):
    order_code = forms.CharField(label="Mã đơn hàng")
    phone_number = forms.CharField(label="Số điện thoại")
