from django.urls import path
from . import views

urlpatterns = [
    path('dat-hang/', views.place_order, name='place_order'),
    path('dat-hang/thanh-cong/<str:order_code>/', views.order_success, name='order_success'),
    path('tra-cuu-don-hang/', views.lookup_order, name='lookup_order'),
]
