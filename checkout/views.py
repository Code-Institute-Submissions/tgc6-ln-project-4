from django.shortcuts import render, reverse, HttpResponse, get_object_or_404

# import settings so that we can access the public stripe key
from django.conf import settings


# Create your views here.
def checkout(request):
    return render(request, 'checkout/checkout.template.html')
