from django.contrib import admin
from .models import Person, Offer


class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock")


class OfferAdmin(admin.ModelAdmin):
    list_display = ("code", "discount")


admin.site.register(Person, PersonAdmin)
admin.site.register(Offer, OfferAdmin)
