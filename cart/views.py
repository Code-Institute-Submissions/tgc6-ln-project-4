from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from django.contrib import messages
from products.models import Product

# Create your views here.
def add_to_cart(request, product_id):
    # load in the cart details
    cart = request.session.get('shopping_cart', {})
    final_total = 0
    
    # we check if the product_is not in the cart. If so, we will add it
    if product_id not in cart:
        product = get_object_or_404(Product, pk=product_id)
        # product is found, let's add it to the cart

        cart[product_id] = {
            'id': product_id,
            'name': product.name,
            'cost': format(float(product.selling_price),'.2f'),
            'qty': 1,
            'total_cost' : format(float(product.selling_price),'.2f'),
        }

        # save the cart back to sessions
        request.session['shopping_cart'] = cart
        messages.success(request, "product has been added to your cart!")
        # return redirect(reverse('view_cart'))
    else:
        cart[product_id]['qty'] +=1
        cart[product_id]['total_cost'] = format( (float(cart[product_id]['cost']) * cart[product_id]['qty'] ),'.2f')
        # save the cart back to sessions
        request.session['shopping_cart'] = cart

        # return HttpResponse('Product added')
    return redirect(reverse('view_cart'))

def view_cart(request):
    # retrieve the cart
    cart = request.session.get('shopping_cart', {})
    sum = 0
    
    for item in cart:
        product_total = cart[ item ]['total_cost']
        sum = format( float(sum) + float(product_total), '.2f')

    return render(request, 'cart/view_cart.template.html', {
        'cart': cart,
        'final_total' : sum
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
    cart[product_id]['total_cost'] = format( (float(cart[product_id]['cost']) * cart[product_id]['qty'] ),'.2f')
    # save the cart back to sessions
    request.session['shopping_cart'] = cart
    # messages.success(request, f"Quantity for {cart[product_id]['qty']} has been changed")
    return render(request, 'cart/view_cart.template.html', {
        'cart': cart
    })

def minus_number(request, product_id):
    cart = request.session.get('shopping_cart', {})
    if cart[product_id]['qty'] == 1:
        del cart[product_id]
    else:
        cart[product_id]['qty'] -=1
        cart[product_id]['total_cost'] = format( (float(cart[product_id]['cost']) * cart[product_id]['qty'] ),'.2f')
    # save the cart back to sessions
    request.session['shopping_cart'] = cart
    return render(request, 'cart/view_cart.template.html', {
        'cart': cart
    })
