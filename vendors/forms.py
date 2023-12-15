from django.forms import ModelForm
from django import forms
from shop.models import Product
from vendors.models import Vendor


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'image', 'image1','image2', 'image3', 'stock', 'price']



class VendorCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VendorCreationForm, self).__init__(*args, **kwargs)

        self.fields['account_name'].widget.attrs['class'] = 'input'
        self.fields['bank_IBAN'].widget.attrs['class'] = 'input'
        self.fields['bank_name'].widget.attrs['class'] = 'input'
        self.fields['bank_bic'].widget.attrs['class'] = 'input'
        self.fields['county'].widget.attrs['class'] = 'input'
        self.fields['gender'].widget.attrs['class'] = 'input'

    class Meta:
        model = Vendor
        fields = '__all__'
        exclude = ('user', 'is_vendor', 'is_approved', 'created_at', 'last_login')
        

