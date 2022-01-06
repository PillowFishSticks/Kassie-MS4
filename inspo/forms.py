# Imports
# 3rd party:
from django import forms

# Internal:
from .models import Inspo
from products.widgets import CustomClearableFileInput


class InspoForm(forms.ModelForm):
    """
    A class for the inspo form
    """
    class Meta:
        model = Inspo
        fields = ('title', 'inspo_item_text', 'image', 'status')

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput)
