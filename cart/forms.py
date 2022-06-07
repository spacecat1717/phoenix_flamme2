from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

#SIZE_CHOISES = [('SM', 'Small'), ('ST', 'Standart')]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    size = forms.BooleanField(required=False, initial=False)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
