"""Forms of the project."""
from django import forms
from .models import Thing


# Create your forms here.

class ThingForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'maxlength': '120'}))

    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
