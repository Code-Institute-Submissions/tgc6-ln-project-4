from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from django.views.decorators.csrf import csrf_exempt
from products.views import index

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


@csrf_exempt
def completed(request):
    payload = request.body
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    event = None

    try:
        event = stripe.Webhook.construct_event(
        payload, sig_header, endpoint_secret
             )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
        # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        # Fulfill the purchase...
        handle_payment(session)
    return HttpResponse(status=200)


def charge(request):
    if request.method == 'GET':
        amount = 100
        # or
        # request.GET['amount']
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
