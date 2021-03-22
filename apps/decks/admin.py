from django.contrib import admin
from .models import Decks


class DeckAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


admin.site.register(Decks, DeckAdmin)
