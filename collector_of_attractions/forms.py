from django import forms


CATEGORY = (
    ('Muzeum', 'Muzeum'),
    ('Kościół', 'Kościół'),
    ('Zamek', 'Zamek'),
    ('Pomnik', 'Pomnik'),
    ('Galeria Sztuki', 'Galeria Sztuki'),
    ('Obraz', 'Obraz'),
)


class AttractionCreateForm(forms.Form):
    name                = forms.CharField()
    category            = forms.ChoiceField(choices=CATEGORY)
    short_description   = forms.TextField()
    long_description    = forms.TextField(requierd=False)