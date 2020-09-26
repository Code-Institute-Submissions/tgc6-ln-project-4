from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.template.html', {
        'products': products
    })


def view_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/view_details.template.html', {
        'product': product
    })


def about(request):
    return render(request, 'products/about.template.html')

def show_product(request):
    return render(request, 'products/show_prduct.templates.html')