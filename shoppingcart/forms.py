from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


PAYMENT_CHOICES = (
    ('S', 'Stripe'),
)

class CheckoutForm(forms.Form):
    """Checkout form details"""
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '1234 Main St'
    }))
    appartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Appartment or suite'
    }))
    country = CountryField(blank_label='(select country)').formfield(
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100'
        }))
    zip_code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    same_shipping_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)
        
        
class CouponForm(forms.Form):
    """Coupon form that takes a code"""
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))
    

class RefundForm(forms.Form):
    """
    Refund form with the reference code
    and a message
    """
    ref_code = forms.CharField()
    message = forms.Textarea()
    email = forms.EmailField()
    
    
    
    