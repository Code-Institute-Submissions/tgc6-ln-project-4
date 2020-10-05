from django.shortcuts import render, reverse, HttpResponse, get_object_or_404

# import settings so that we can access the public stripe key
from django.conf import settings
import stripe

from products.models import Product
from django.contrib.sites.models import Site

# Create your views here.
def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    cart = request.session.get('shopping_cart', {})

    return render(request, 'checkout/checkout.template.html')

def success(request):
    

    return render(request, 'checkout/success.template.html')

def cancelled(request):

    return render(request, 'checkout/cancelled.template.html')
