from django.contrib import admin

from collector_of_attractions.models import Attraction, AttractionAddress, AttractionImages, AttractionStatus


class AttractionStatusTabularInLine(admin.TabularInline):
    model = AttractionStatus


class AttractionImagesTabularInLine(admin.TabularInline):
    model = AttractionImages


class AttractionAddressTabularInLine(admin.TabularInline):
    model = AttractionAddress


class AttractionAdmin(admin.ModelAdmin):
    inlines = [AttractionAddressTabularInLine, AttractionStatusTabularInLine, AttractionImagesTabularInLine]
    class Meta:
        model = Attraction


admin.site.register(Attraction, AttractionAdmin)


