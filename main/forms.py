from django import forms
from .models import Item


SIZES = (
    ("mini", "10 gr"),
    ("standart", "20 gr"),
)


class AddForm(forms.ModelForm):
    """Form for adding items to cart"""
    class Meta:
        model = Item
        quantity = forms.NumberInput()
        small = forms.ChoiceField(required=True, choices=SIZES)
        fields = ['quantity', 'small'] 
        