from django import forms
from .models import Feeding

class FeedingForm(forms.ModelForm):
    # meta configuration variable for your class
    # this is just the way django has defined it
    class Meta:
        model = Feeding
        fields = ['date', 'meal']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            )
        }