from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from collection.models import CollectionItem
from pokemonCard.models import PokemonCard
from .models import UserProfile  # import your UserProfile

# Inline that lets you add/edit Pokémon for a user
class CollectionItemInline(admin.TabularInline):
    model = CollectionItem
    extra = 0
    autocomplete_fields = ['pokemon']
    readonly_fields = ['date']

# Inline that lets you edit pokeCoins for a user
class PokeCoinInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'PokeCoins'
    fields = ('pokeCoins',)

# Override the default User admin
class CustomUserAdmin(UserAdmin):
    inlines = [PokeCoinInline, CollectionItemInline] # ALL FUTURE INLINES GO HERE PLEASE

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
