from django import forms
from .models import Product
from .models import outgoing_supply
from .models import incoming
from datetime import datetime
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
        model = outgoing_supply
        #product_id=forms.ModelChoiceField(queryset=Product.objects.order_by('product_id').values_list('id', flat=True).distinct())
        fields = ('product_id', 'engg_name', 'quantity', 'date')
        #forms.ModelChoiceField(queryset=Product.objects.order_by('id').values_list('id', flat=True).distinct())

action = (
    ('Incoming', 'Incoming Transactions'),
    ('Outgoing', 'Outgoing Transactions'),)

class historyForm(forms.Form):
    #class Meta:
    search_content= forms.CharField(max_length=100, required = False, label='Incoming (Name/Cetagory/Supplier/Description) Outgoing (Product_id/Engineer)')
    start = forms.DateField(input_formats=['%Y-%m-%d'], required = False, label="Start Date (YYYY-MM-DD)")
    end = forms.DateTimeField(input_formats=['%Y-%m-%d'], required = False, label="End Date (YYYY-MM-DD)")
    option = forms.ChoiceField(choices=action, required=True)