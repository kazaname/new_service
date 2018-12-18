from django import forms

from .models import Attraction

# CATEGOTY=(
#     ('Monument','Monument'),
#     ('Painting', 'Painting'),
#     ('Church', 'Church'),
#     ('Sculpture', 'Sculpture'),
#     ('Museum', 'Museum'),
# )
#
# class AttractionsCreateForm(forms.Form):
#     name = forms.CharField()
#     category = forms.ChoiceField(choices=CATEGOTY)
#     author = forms.CharField(required=False)
#     short_description = forms.CharField(max_length=500)
#     long_description = forms.CharField(required=False)
#
#     def clean_name(self):
#         name = self.cleaned_data.get("name")
#         if name == "Hello":
#             raise forms.ValidationError("Not a valid name")
#         return name


class AttractionCreateModelFrom(forms.ModelForm):
    class Meta:
        model = Attraction
        fields = [
            'owner',
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