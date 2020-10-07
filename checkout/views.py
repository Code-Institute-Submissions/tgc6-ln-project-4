from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from django.views.decorators.csrf import csrf_exempt
from products.views import index

# import settings so that we can access the public stripe key
from django.conf import settings
import stripe

from products.models import Product
from django.contrib.sites.models import Site

# Create your views here.


def charge(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    # cart = request.session.get('shopping_cart', {})
    # request.session['shopping_cart'] = cart
    
    if request.method == 'GET':
        amount = 100
        key = settings.STRIPE_PUBLISHABLE_KEY  # 1
        return render(request, 'checkout/charge.template.html', {
        'key': key,
        'amount': amount
        })
    else:
        stripe.api_key = settings.STRIPE_SECRET_KEY #2
        charge = stripe.Charge.create(           
            amount= 100,            
            currency='sgd',           
            description='A Django charge',         
            source=request.POST['stripeToken']       
        )     
        request.session['shopping_cart'] = {}
        return redirect(reverse(index))
