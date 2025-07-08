from django.shortcuts import render, redirect
from .forms import OrderForm, OrderItemForm
from .models import Order, OrderItem
from products.models import PriceTier
from django.utils.crypto import get_random_string
from django.shortcuts import get_object_or_404
from .forms import OrderLookupForm

def place_order(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        item_form = OrderItemForm(request.POST, request.FILES)

        if order_form.is_valid() and item_form.is_valid():
            order = order_form.save(commit=False)
            order.order_code = 'STT' + get_random_string(6).upper()
            order.save()

            price = PriceTier.objects.filter(
                product=item_form.cleaned_data['product'],
                paper_type=item_form.cleaned_data['paper_type'],
                size=item_form.cleaned_data['size'],
                quantity=item_form.cleaned_data['quantity']
            ).first()

            item = OrderItem.objects.create(
                order=order,
                product=item_form.cleaned_data['product'],
                paper_type=item_form.cleaned_data['paper_type'],
                size=item_form.cleaned_data['size'],
                quantity=item_form.cleaned_data['quantity'],
                price=price.price if price else 0,
                file_upload=item_form.cleaned_data['file_upload']
            )

            return redirect('order_success', order_code=order.order_code)

    else:
        order_form = OrderForm()
        item_form = OrderItemForm()

    return render(request, 'orders/order_form.html', {
        'order_form': order_form,
        'item_form': item_form,
    })

def order_success(request, order_code):
    qr_bank_image = "/static/qr_vietcombank.png"  # đường dẫn ảnh QR
    return render(request, 'orders/order_success.html', {
        'order_code': order_code,
        'qr_image': qr_bank_image,
    })


def lookup_order(request):
    result = None
    if request.method == 'POST':
        form = OrderLookupForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['order_code']
            phone = form.cleaned_data['phone_number']

            try:
                order = Order.objects.get(order_code=code, phone_number=phone)
                result = order
            except Order.DoesNotExist:
                result = 'not_found'
    else:
        form = OrderLookupForm()

    return render(request, 'orders/lookup_order.html', {
        'form': form,
        'result': result
    })