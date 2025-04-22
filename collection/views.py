import requests
from django.shortcuts import render, get_object_or_404

from pokemonCard.models import PokemonCard

def get_cards(request):
    pokemon_list = PokemonCard.objects.all()
    return render(request, 'collection/index.html', {'pokemon_list': pokemon_list})
