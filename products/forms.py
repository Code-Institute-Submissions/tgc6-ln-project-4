from django import forms
from .models import Product
from cloudinary.forms import CloudinaryJsFileField


class ProductForm(forms.ModelForm)
 class Meta:
        model = Product
       # tuple are in round parenthesis
       # they are like lists in python
       # once we put something in a tuple, we cannot change the tuple anymore
        fields = ('name', 'selling_price', 'quantity', 'pic')
 pic = CloudinaryJsFileField()
