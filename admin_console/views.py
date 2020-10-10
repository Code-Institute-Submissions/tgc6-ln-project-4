from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from products.models import Product
from admin_console.forms import AddProductForm

# Create your views here.
def admin_panel(request):
    products = Product.objects.all()
    return render(request, 'admin_console/admin_panel.template.html', {
        'products' : products,
    })

def admin_add(request):
    if request.method == 'POST':
        create_form = AddProductForm(request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect(reverse(admin_panel))

        else:
            return render(request, 'admin_console/admin_add.template.html', {
                'form': create_form
            })
    
    else:
        create_form = AddProductForm()
        return render(request, 'admin_console/admin_add.template.html', {
            'form': create_form})

