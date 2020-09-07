from django.shortcuts import render
from .models import Product


# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.template.html', {
        'products': products
    })
