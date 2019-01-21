from django import forms

from .models import SignUp


CATEGORY = (
    ('----', '----'),
    ('Opinia', 'Opinia'),
    ('Sugestia', 'Sugestia'),
    ('Błąd', 'Błąd'),
    ('Inna', 'Inna'),
)

class ContactForm(forms.Form):
    full_name = forms.CharField()
    category = forms.ChoiceField(choices=CATEGORY, label="Category", initial='', widget=forms.Select())
    # full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()

    # Walidacja działa w ten sam sposób jak w przypadku poniżej
    def clean_category(self):
        category = self.cleaned_data.get('category')

        if '----' in category:
            raise forms.ValidationError("Proszę o wybranie kategorii rozwijanej listy.")


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def clean_email(self):
       email = self.cleaned_data.get('email')
       email_base, provider = email.split("@")
       domain, extension = provider.split(".")

       if not "edu" in extension:
           raise forms.ValidationError("Please use a valid .edu email address")
       return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name")
        # validation code
        return full_name
