from django.contrib import admin

from .models import Attraction, AttractionAddress, AttractionImages, AttractionStatus


class AttractionStatusTabularInLine(admin.TabularInline):
    model = AttractionStatus


class AttractionImagesTabularInLine(admin.TabularInline):
    model = AttractionImages


class AttractionAddressTabularInLine(admin.TabularInline):
    model = AttractionAddress


class AttractionAdmin(admin.ModelAdmin):
    inlines = [AttractionAddressTabularInLine, AttractionStatusTabularInLine, AttractionImagesTabularInLine]
    list_display = ['name', 'owner', 'category', 'author', 'slug', 'timestamp', 'upload']
    class Meta:
        model = Attraction


admin.site.register(Attraction, AttractionAdmin)
