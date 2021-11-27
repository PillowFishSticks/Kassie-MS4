from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """ A form for users to add a review to product """

    class Meta:
        model = Review
        exclude = (
            'user',
            'date_created',
            'product')

        fields = [
            'title',
            'description',
            ]