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
            'cost': float(round(product.selling_price,2)),
            'qty': 1,
            'total_cost' : float(round(product.selling_price,2)),
        }

        # save the cart back to sessions
        request.session['shopping_cart'] = cart

        messages.success(request, "product has been added to your cart!")
        # return redirect(reverse('view_cart'))
    else:
        cart[product_id]['qty'] +=1
        cart[product_id]['total_cost'] = cart[product_id]['cost'] * cart[product_id]['qty']
        # save the cart back to sessions
        request.session['shopping_cart'] = cart

        # return HttpResponse('Product added')
    return redirect(reverse('view_cart'))

def view_cart(request):
    # retrieve the cart
    cart = request.session.get('shopping_cart', {})
    return render(request, 'cart/view_cart.template.html', {
        'cart': cart
    })

def remove_from_cart(request, product_id):
    cart = request.session.get('shopping_cart', {})

    if product_id in cart:
        del cart[product_id]
        request.session['shopping_cart'] = cart
        messages.success(request, "Item removed from cart successfully!")
    return redirect(reverse('view_cart'))

def add_number(request, product_id):
    cart = request.session.get('shopping_cart', {})
    cart[product_id]['qty'] +=1
    cart[product_id]['total_cost'] = cart[product_id]['cost'] * cart[product_id]['qty']
    # save the cart back to sessions
    request.session['shopping_cart'] = cart
    return render(request, 'cart/view_cart.template.html', {
        'cart': cart
    })

def minus_number(request, product_id):
    cart = request.session.get('shopping_cart', {})
    if cart[product_id]['qty'] == 1:
        del cart[product_id]
    else:
        cart[product_id]['qty'] -=1
        cart[product_id]['total_cost'] = cart[product_id]['cost'] * cart[product_id]['qty']
    # save the cart back to sessions
    request.session['shopping_cart'] = cart
    return render(request, 'cart/view_cart.template.html', {
        'cart': cart
    })
