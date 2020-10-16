from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from products.models import Product
from admin_console.forms import AddProductForm, EditProductForm
from django.contrib.auth.decorators import login_required
from products.views import index

# Create your views here.
@login_required    
def admin_panel(request):
    if request.user.is_superuser:
        products = Product.objects.all()
        return render(request, 'admin_console/admin_panel.template.html', {
            'products' : products,
        })
    else:
        return redirect(reverse(index))


@login_required    
def admin_add(request):
    if request.user.is_superuser:
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
    else:
        return redirect(reverse(index))


@login_required    
def admin_edit(request, product_id):
    if request.user.is_superuser:
        product = get_object_or_404(Product, pk=product_id)
        if request.method == "POST":
            edit_form = AddProductForm(request.POST, instance=product)
            print(edit_form)

            if edit_form.is_valid():
                print("................Save Entry...........")
                print(edit_form)
                edit_form.save()
                return redirect(reverse(admin_panel))
            else:
                return render(request, 'admin_console/admin_edit.template.html', {
                "form": edit_form
            })
        else:
            edit_form = AddProductForm(instance=product)
            return render(request, 'admin_console/admin_edit.template.html', {
            "form": edit_form,
            })
    else:
        return redirect(reverse(index))


@login_required    
def admin_remove (request, product_id):
    if request.user.is_superuser:
        product = get_object_or_404(Product, pk=product_id)
        if request.method == 'POST':
            product.delete()
            return redirect(reverse(admin_panel))
        else :
            return render(request, 'admin_console/admin_remove.template.html', {
                'product' : product
            })
    else:
        return redirect(reverse(index))