from django import forms
from .models import Item

class CartItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item