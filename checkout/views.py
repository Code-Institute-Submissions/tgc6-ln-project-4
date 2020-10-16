from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from django.views.decorators.csrf import csrf_exempt
from products.views import index
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# import settings so that we can access the public stripe key
from django.conf import settings
import stripe

from products.models import Product
from django.contrib.sites.models import Site

# Create your views here.
@login_required    
def charge(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    # cart = request.session.get('shopping_cart', {})
    # request.session['shopping_cart'] = cart
    cart = request.session.get('shopping_cart', {})
    sum = 0
    # Sum up the total to be charged
    for item in cart:
        product_total = cart[ item ]['total_cost']
        sum = sum + float(product_total)

    # Stripe charge script
    if request.method == 'GET':
        amount = sum * 100
        key = settings.STRIPE_PUBLISHABLE_KEY  # 1
        return render(request, 'checkout/charge.template.html', {
        'key': key,
        'amount': sum * 100,
        'cart' : cart,
        'final_total' : format(sum,'.2f')
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
        messages.success(request, "Thank you for making the purchase! You will receive your items within 7 working days")

        return redirect(reverse(index))
