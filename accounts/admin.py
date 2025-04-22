
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from collection.models import CollectionItem
from pokemonCard.models import PokemonCard

# Inline that lets you add/edit Pokémon for a user
class CollectionItemInline(admin.TabularInline):
    model = CollectionItem
    extra = 0
    autocomplete_fields = ['pokemon']
    readonly_fields = ['date']

# Override the default User admin
class CustomUserAdmin(UserAdmin):
    inlines = [CollectionItemInline]

admin.site.unregister(User)

admin.site.register(User, CustomUserAdmin)
