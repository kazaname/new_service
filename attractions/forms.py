from django import forms

from .models import Attraction, AttractionAddress, AttractionStatus


class AttractionFrom(forms.ModelForm):

    class Meta:
        model = Attraction
        fields = [
            'name',
            'category',
            'author',
            'short_description',
            'long_description',
        ]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name


class AttractionAddressForm(forms.ModelForm):

    class Meta:
        model = AttractionAddress

        fields = [
            'country',
            'province',
            'city',
            'street',
            'latitude',
            'longitude',
        ]
