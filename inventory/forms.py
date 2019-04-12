from django import forms
from .models import Product
from .models import outgoing
from .models import incoming

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'cetagory', 'supplier', 'unit_price', 'quantity', 'date', 'description')

class IncomingForm(forms.ModelForm):

    class Meta:
        model = incoming
        fields = ('name', 'cetagory', 'supplier', 'unit_price', 'quantity', 'date', 'description')
        
class OutgoingForm(forms.ModelForm):

    class Meta:
        model = outgoing
        fields = ('product_id', 'engg_name', 'quantity', 'date')
