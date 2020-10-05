from django.urls import path
import checkout.views

urlpatterns = [
    path('', checkout.views.checkout, name='checkout'),
    path('success/', checkout.views.success, name='success'),
    path('cancelled/', checkout.views.cancelled, name='cancelled'),
]