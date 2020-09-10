from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse, HttpResponseRedirect
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_cart(request):
    # retrieve the cart
    cart = request.session.get('shopping_cart', {})
    total = 0
    for k, v in cart.items():
        total += float(v['cost']) * int(v['qty'])

    context = {
        'total': float("{:.2f}".format(total)),
        'name': 'View Cart',
        'cart': cart
    }

    return render(request, 'cart/view_cart.template.html', context)
