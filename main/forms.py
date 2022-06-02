from django import forms



SIZES = (
    ("mini", "10 gr"),
    ("standart", "20 gr"),
)


class AddForm(forms.ModelForm):
    """Form for adding items to cart"""
    
        