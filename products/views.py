from django.shortcuts import render
from .models import Product


# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.template.html', {
        'products': products
    })

def view_product_details(request):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/details.template.html', {
        'products': products
    })

def about(request):
    return render(request, 'products/about.template.html')
