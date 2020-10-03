from django.urls import path
import checkout.views

urlpatterns = [
    path('checkout/', checkout.views.checkout, name='checkout'),
]