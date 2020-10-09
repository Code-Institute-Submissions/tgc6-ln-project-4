from django.shortcuts import render, get_object_or_404
from products.models import Product

# Create your views here.
def admin_panel(request):
    products = Product.objects.all()
    return render(request, 'admin_console/admin_panel.template.html', {
        'products' : products,
    })