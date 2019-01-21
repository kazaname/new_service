from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save

from .utils import unique_slug_generator
from .validators import validate_category, validate_text


CATEGORY = (
    ('Monument', 'Monument'),
    ('Painting', 'Painting'),
    ('Church', 'Church'),
    ('Sculpture', 'Sculpture'),
    ('Museum', 'Museum'),
)


class Attraction(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=100, validators=[validate_text])
    category = models.CharField(choices=CATEGORY, max_length=20, validators=[validate_category, validate_text])
    author = models.CharField(max_length=120, blank=True, null=True, validators=[validate_text])
    short_description = models.TextField(max_length=500, validators=[validate_text])
    long_description = models.TextField(blank=True, null=True, validators=[validate_text])
    slug = models.SlugField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    upload = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name

    class Meta:
        ordering = ['-upload', '-timestamp']



class AttractionStatus(models.Model):
    attraction = models.OneToOneField(Attraction, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    points = models.IntegerField()
    is_dublicated = models.BooleanField(default=False)

    def __str__(self):
        return self.attraction.name + ', Activated: ' + str(self.is_active)

class AttractionAddress(models.Model):
    attraction = models.OneToOneField(Attraction, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    latitude = models.FloatField(max_length=20)  # Szerokość geograficzna
    longitude = models.FloatField(max_length=20)  # Długość geograficzna

    def __str__(self):
        return self.attraction.name + ' ' + self.country + ' ' + self.city


class AttractionImages(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploaded_pictures/', )
    timestamp = models.DateTimeField(auto_now_add=True)


def attraction_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.name = instance.name.title()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(attraction_pre_save_receiver, sender=Attraction)
