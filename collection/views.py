from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from collection.models import CollectionItem
from pokemonCard.models import PokemonCard

@login_required
def user_collection(request):
    cards = CollectionItem.objects.filter(user=request.user, status='collection').select_related('pokemon')
    return render(request, 'collection/index.html', {
        'user_pokemon_list': cards
    })