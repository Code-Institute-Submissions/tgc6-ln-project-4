from django.shortcuts import render, HttpResponse, get_object_or_404, redirect,reverse, HttpResponseRedirect
from django.contrib import messages
from products.models import Product

# Create your views here.


def add_to_cart(request, product_id):
    cart = request.session.get('shopping_cart', {})
    if product_id not in cart:
        product = get_object_or_404(Product, pk=product_id)
        # product is found, add it to the cart
        cart[product_id] = {
            'id': product_id,
            'name': product.name,
            'cost': float(product.selling_price),
            'qty': 1,
            'total_cost': float(product.selling_price),
        }
        # save the cart back to sessions
        request.session['shopping_cart'] = cart

        messages.success(
            request, f"{cart[product_id]['nome']} has been added to your cart!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        cart[product_id]['qty'] = int(cart[product_id]['qty']) + 1
        cart[product_id]['total_cost'] = float(
            cart[product_id]['total_cost']) + float(cart[product_id]['cost'])
        request.session['shopping_cart'] = cart
        messages.success(
            request, f"{cart[product_id]['name']} has been added to your cart!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


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
