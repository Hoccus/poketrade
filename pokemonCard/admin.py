from django.contrib import admin
from .models import PokemonCard

@admin.register(PokemonCard)
class PokemonCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'hp', 'attack', 'defense')
    search_fields = ('name',)
