from django.contrib import admin
from django.utils.html import format_html
from .models import CollectionItem
admin.site.register(CollectionItem)

class CollectionItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'pokemon', 'status', 'pokemon_image', 'date')
    list_filter = ('status', 'user')
    search_fields = ('pokemon__name', 'user__username')

    def pokemon_image(self, obj):
        return format_html('<img src="{}" width="60" />', obj.pokemon.image_url)

    pokemon_image.short_description = 'Image'
