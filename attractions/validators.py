from django.core.exceptions import ValidationError

from .vulgarity_list import vulgarity_pl

CATEGORY = ['Monument', 'Painting', 'Church', 'Sculpture', 'Museum']


def validate_category(value):

    if value not in CATEGORY:
        raise ValidationError("{value} is not a valid category".format(value=value))


def validate_text(value):
    text = value.split()
    for word in text:
        lower_word = word.lower()
        if word in vulgarity_pl or lower_word in vulgarity_pl:
            raise ValidationError("Vulgarity is not accepted. Please chenge {word} !!!".format(word=word))
