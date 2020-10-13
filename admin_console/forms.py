from django import forms
from products.models import Product
from cloudinary.forms import CloudinaryJsFileField

# class AddProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ('name', 'selling_price', 'quantity', 'pic')
#     pic = CloudinaryJsFileField()

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'selling_price', 'quantity', 'cover')
    cover = CloudinaryJsFileField()

class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'selling_price', 'quantity', 'cover')
    cover = CloudinaryJsFileField()