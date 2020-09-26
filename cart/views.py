from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from django.contrib import messages
from products.models import Product

# Create your views here.
def add_to_cart(request, product_id):
    # the second argument will be the default value if
    # if the key does not exist in the session
    cart = request.session.get('shopping_cart', {})
    # we check if the product_is not in the cart. If so, we will add it
    if product_id not in cart:
        product = get_object_or_404(Product, pk=product_id)
        # product is found, let's add it to the cart
        cart[product_id] = {
            'id': product_id,
            'name': product.name,
            'cost': 99,
            'qty': 1
        }

        # save the cart back to sessions
        request.session['shopping_cart'] = cart

        messages.success(request, "product has been added to your cart!")
        # return redirect(reverse('view_cart'))
    else:
        cart[product_id]['qty'] + 1

        # return HttpResponse('Product added')
    return redirect(reverse('view_cart'))

def view_cart(request):
    # retrieve the cart
    cart = request.session.get('shopping_cart', {})

    return render(request, 'cart/view_cart.template.html', {
        'shopping_cart': cart
    })